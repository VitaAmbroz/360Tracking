#################################################################################################
# Visual object tracking in panoramic video
# Master thesis at Brno University of Technology - Faculty of Information Technology
# Author:       Vít Ambrož (xambro15@stud.fit.vutbr.cz)
# Supervisor:   Doc. Ing. Martin Čadík, Ph.D.
# Module:       ocean_360_default.py
# Description:  Default tracking using Ocean tracker
#################################################################################################
# ------------------------------------------------------------------------------
# Copyright (c) Microsoft
# Licensed under the MIT License.
# Email: zhangzhipeng2017@ia.ac.cn
# https://github.com/researchmm/TracKit
# ------------------------------------------------------------------------------

import _init_paths
import os
import sys
import cv2
import torch
import numpy as np

# try:
#     from torch2trt import TRTModule
# except:
#     print('Warning: TensorRT is not successfully imported')

import models.models as models

from os.path import exists, join, dirname, realpath
from tracker.ocean import Ocean
from tracker.online import ONLINE
from easydict import EasyDict as edict
from utils.utils import load_pretrain, cxy_wh_2_rect

# custom modules to improve equirectangular tracking
from boundingbox import BoundingBox
from parser import Parser



class Ocean360Default:
    """Default tracking using Ocean tracker"""
    def __init__(self, resume: str, video_path: str, groundtruth_path: str = None, save_result_path: str = None):
        # Ocean architecture attributes
        self.resume = resume
        self.online = True
        self.arch = "Ocean"

        # other attributes
        self.video_path = video_path
        self.groundtruth_path = groundtruth_path
        if save_result_path:
            self.save_result_path = save_result_path
        else:    
            self.save_result_path = "tmp-result-Ocean.txt"
        
        self.video = None
        self.video_width = None
        self.video_height = None
        self.frame = None
        self.bbox = None
        self.gt_bounding_boxes = []
        self.result_bounding_boxes = []

        # enable parsing/creating methods 
        self.parser = Parser()

        # constants for sizes and positions of opencv circles, rectangles and texts
        self.RECTANGLE_BORDER_PX = 3
        self.FONT_SCALE = 0.75
        self.FONT_WEIGHT = 1
        self.TEXT_ROW1_POS = (30,30)
        self.TEXT_ROW2_POS = (30,60)
        self.TEXT_ROW3_POS = (30,90)
        self.TEXT_ROW4_POS = (30,120)

        self.WINDOW_NAME = "Tracker-Ocean"

    
    def _drawBoundingBox(self, videoWidth, point1, point2, boundingBox, color, thickness):
        """Method for drawing rectangle according to points"""
        if (boundingBox.is_on_border()):
            # draw two rectangles around the region of interest
            rightBorderPoint = (videoWidth - 1, point2[1])
            cv2.rectangle(self.frame, point1, rightBorderPoint, color, thickness)

            leftBorderPoint = (0, point1[1])
            cv2.rectangle(self.frame, leftBorderPoint, point2, color, thickness)
        else:
            # draw a rectangle around the region of interest
            cv2.rectangle(self.frame, point1, point2, color, thickness)


    def _checkBoundsOfPoint(self, point):
        """Checks if given point is in interval [0,self.width] and [0,self.height] with x overflow"""
        # horizontal could overflow in equirectangular
        x = point[0]
        y = point[1]
        if x < 0: 
            x = self.video_width + x - 1
        elif x > self.video_width - 1: 
            x = x - self.video_width - 1
        
        # vertical
        if y < 0: 
            y = 0
        elif y > self.video_height - 1:
            y = self.video_height - 1

        point = (x,y)
        return point


    def _saveResults(self):
        """Method for saving result bounding boxes to .txt file"""
        # creating string result data
        resultData = self.parser.createAnnotations(self.result_bounding_boxes)
        # saving file on drive
        self.parser.saveDataToFile(self.save_result_path, resultData)
        print("File '" + self.save_result_path + "' has been successfully created with total " + str(len(self.result_bounding_boxes)) + " computed frames.")


    def run_ocean_default(self):
        """Method for start Ocean tracking without any modifications"""
        # commented unnecessary tensorflow parameters
        # tracker initialization
        info = edict()
        info.arch = self.arch
        info.dataset = 'VOT2019'
        info.TRT = 'TRT' in self.arch
        info.epoch_test = False

        siam_info = edict()
        siam_info.arch = self.arch
        siam_info.dataset = 'VOT2019'
        siam_info.online = self.online
        siam_info.epoch_test = False
        siam_info.TRT = 'TRT' in self.arch

        siam_info.align = False
        # if siam_info.TRT:
        #     siam_info.align = False

        siam_net = models.__dict__[self.arch](align=siam_info.align, online=self.online)
        siam_tracker = Ocean(siam_info)
        print('===> init Siamese <====')

        # if not siam_info.TRT:
        #     siam_net = load_pretrain(siam_net, args.resume)
        # else:
        #     print("tensorrt toy model: not loading checkpoint")
        
        print(self.resume)
        siam_net = load_pretrain(siam_net, self.resume)
        siam_net.eval()
        siam_net = siam_net.cuda()

        # if siam_info.TRT:
        #     print('===> load model from TRT <===')
        #     print('===> please ignore the warning information of TRT <===')
        #     print('===> We only provide a toy demo for TensorRT. There are some operations are not supported well.<===')
        #     print('===> If you wang to test on benchmark, please us Pytorch version. <===')
        #     print('===> The tensorrt code will be contingously optimized (with the updating of official TensorRT.)<===')
        #     trtNet = reloadTRT()
        #     siam_net.tensorrt_init(trtNet)

        if self.online:
            online_tracker = ONLINE(info)
        else:
            online_tracker = None

        print('[*] ======= Track video with {} ======='.format(self.arch))

        self._track_video(siam_tracker, online_tracker, siam_net)


    def _track_video(self, siam_tracker, online_tracker, siam_net):
        ########## 1) Video Checking ##########
        # Read video
        self.video = cv2.VideoCapture(self.video_path)
        # Exit if video not opened.
        if not self.video.isOpened():
            print("Could not open video")
            print(help)
            sys.exit(-1)

        # Read first frame.
        ok, self.frame = self.video.read()
        if not ok:
            print("Error - Could not read a video file")
            sys.exit(-1)

        # save video width/height to global variables
        self.video_width = int(self.video.get(cv2.CAP_PROP_FRAME_WIDTH))
        self.video_height = int(self.video.get(cv2.CAP_PROP_FRAME_HEIGHT))


        ########## 2) Setup opencv2 window ##########
        # resize window (lets define max width is 1600px)
        if self.video_width < 1600:
            cv2.namedWindow(self.WINDOW_NAME)
        else:
            cv2.namedWindow(self.WINDOW_NAME, cv2.WINDOW_NORMAL | cv2.WINDOW_KEEPRATIO)
            whRatio = self.video_width / self.video_height
            if whRatio == 2:
                # pure equirectangular 2:1
                cv2.resizeWindow(self.WINDOW_NAME, 1600, 800)
            else:
                # default 16:9
                cv2.resizeWindow(self.WINDOW_NAME, 1600, 900)

            scaleFactor = self.video_width / 1600
            self.RECTANGLE_BORDER_PX = int(self.RECTANGLE_BORDER_PX * scaleFactor)
            self.FONT_SCALE = self.FONT_SCALE * scaleFactor
            self.FONT_WEIGHT = int(self.FONT_WEIGHT * scaleFactor) + 1
            self.TEXT_ROW1_POS = (int(self.TEXT_ROW1_POS[0] * scaleFactor), int(self.TEXT_ROW1_POS[1] * scaleFactor))
            self.TEXT_ROW2_POS = (int(self.TEXT_ROW2_POS[0] * scaleFactor), int(self.TEXT_ROW2_POS[1] * scaleFactor))
            self.TEXT_ROW3_POS = (int(self.TEXT_ROW3_POS[0] * scaleFactor), int(self.TEXT_ROW3_POS[1] * scaleFactor))
            self.TEXT_ROW4_POS = (int(self.TEXT_ROW4_POS[0] * scaleFactor), int(self.TEXT_ROW4_POS[1] * scaleFactor))

        # use copy of frame to be shown in window
        frame_disp = self.frame.copy()


        ########## 3) Initialation of bounding box ##########
        # Set up initial bounding box
        self.bbox = None
        self.result_bounding_boxes = []
        self.gt_bounding_boxes = []
        if self.groundtruth_path:
            # use first bounding box from given groundtruth
            self.gt_bounding_boxes = self.parser.parseGivenDataFile(self.groundtruth_path, self.video_width)

            if len(self.gt_bounding_boxes) > 0:
                bb1 = self.gt_bounding_boxes[0]
                if bb1.is_annotated:
                    self.bbox = (bb1.get_point1_x(), bb1.get_point1_y(), bb1.get_width(), bb1.get_height())
                    self.result_bounding_boxes.append(bb1)
                else:
                    print("Error - Invalid first frame annotation from file: '" + self.groundtruth_path + "'")
                    sys.exit(-1)
        else:
            # using opencv2 select ROI
            cv2.putText(frame_disp, 'Select target ROI and press ENTER', self.TEXT_ROW1_POS, cv2.FONT_HERSHEY_SIMPLEX, self.FONT_SCALE, (0, 200, 250), self.FONT_WEIGHT)

            x, y, w, h = cv2.selectROI(self.WINDOW_NAME, frame_disp, False)
            self.bbox = [x, y, w, h]

            # save it to result list
            p1 = (int(self.bbox[0]), int(self.bbox[1]))
            p2 = (int(self.bbox[0] + self.bbox[2]), int(self.bbox[1] + self.bbox[3]))
            # new instance of bounding box
            bb1 = BoundingBox(p1, p2, self.video_width)
            bb1.is_annotated = True
            self.result_bounding_boxes.append(bb1)

        if not(self.bbox) or self.bbox == (0,0,0,0):
            print("Error - Invalid first frame annotation")
            sys.exit(-1)


        ########## 4) Tracking process ##########
        # prints just basic guide and info
        print("--------------------------------------------------------------------")
        print("Ocean default tracking process has started...")
        print("Tracker  : Ocean")
        print("Frame #1 : " + str(self.bbox))
        print("Press 'Esc' or 'Q' key to exit")
        print("--------------------------------------------------------------------")

        # initialize tracker with first frame and bounding box
        lx, ly, w, h = self.bbox[0], self.bbox[1], self.bbox[2], self.bbox[3]
        target_pos = np.array([lx + w/2, ly + h/2])
        target_sz = np.array([w, h])

        state = siam_tracker.init(self.frame, target_pos, target_sz, siam_net)  
        if self.online:
            rgb_im = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
            # NEED constant for resume..
            resume_path = "snapshot/OceanV19on.pth"
            online_tracker.init(self.frame, rgb_im, siam_net, target_pos, target_sz, True, dataname='VOT2019', resume=resume_path)

        # display first frame
        cv2.imshow(self.WINDOW_NAME, frame_disp)

        # if you want to have the FPS according to the video then uncomment this code
        # fps = cap.get(cv2.CAP_PROP_FPS)
        videoFPS = 30
        # calculate the interval between frame
        interval = int(1000/videoFPS) 

        while True:
            # Read a new frame
            ok, self.frame = self.video.read()
            if not ok:
                break

            # Start timer
            timer = cv2.getTickCount()

            # update tracker
            if self.online:
                rgb_im = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
                state = online_tracker.track(self.frame, rgb_im, siam_tracker, state)
            else:
                state = siam_tracker.track(state, self.frame)

            location = cxy_wh_2_rect(state['target_pos'], state['target_sz'])
            self.bbox = [int(location[0]), int(location[1]), int(location[2]), int(location[3])]

            # Calculate Frames per second (FPS)
            fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer)

            # draw bounding box
            if self.bbox[0] and self.bbox[1] and self.bbox[2] and self.bbox[3]:
                # Tracking success
                p1 = (self.bbox[0], self.bbox[1])
                p2 = (self.bbox[0] + self.bbox[2], self.bbox[1] + self.bbox[3])

                p1 = self._checkBoundsOfPoint(p1)
                p2 = self._checkBoundsOfPoint(p2)

                # new instance of bounding box
                bb = BoundingBox(p1, p2, self.video_width)
                bb.is_annotated = True
                self.result_bounding_boxes.append(bb)

                # draw bounding box to original frame
                self._drawBoundingBox(self.video_width, p1, p2, bb, (0, 255, 0), self.RECTANGLE_BORDER_PX)
            else:                
                # tracking failure
                cv2.putText(self.frame, "Tracking failure detected", self.TEXT_ROW4_POS, cv2.FONT_HERSHEY_SIMPLEX, self.FONT_SCALE, (0, 0, 255), self.FONT_WEIGHT)
                
                # new instance of bounding box
                bb = BoundingBox(None, None, self.video_width)
                bb.is_annotated = False
                self.result_bounding_boxes.append(bb)

            
            # Display tracker type on frame
            cv2.putText(self.frame, "Ocean Tracker", self.TEXT_ROW1_POS, cv2.FONT_HERSHEY_SIMPLEX, self.FONT_SCALE, (0, 200, 250), self.FONT_WEIGHT)
            # Display FPS on frame
            cv2.putText(self.frame, "Video   FPS : " + str(videoFPS), self.TEXT_ROW2_POS, cv2.FONT_HERSHEY_SIMPLEX, self.FONT_SCALE, (0, 250, 0), self.FONT_WEIGHT)
            cv2.putText(self.frame, "Tracker FPS : " + str(int(fps)), self.TEXT_ROW3_POS, cv2.FONT_HERSHEY_SIMPLEX, self.FONT_SCALE, (0, 250, 0), self.FONT_WEIGHT)
            # Display result
            cv2.imshow(self.WINDOW_NAME, self.frame)
            

            # waitKey time computing
            # time in ms
            time = int(1000 * (cv2.getTickCount() - timer) / cv2.getTickFrequency())

            waitMiliseconds = 1
            if (time >= interval):
                waitMiliseconds = 1
            else:
                waitMiliseconds = interval - time
            
            k = cv2.waitKey(waitMiliseconds) & 0xff
            # Exit if 'Esc' or 'q' key is pressed
            if k == 27 or k == ord("q"): 
                break

        # always save tracker result
        self._saveResults()

        self.video.release()
        cv2.destroyAllWindows()