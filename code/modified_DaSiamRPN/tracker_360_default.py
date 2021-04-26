# --------------------------------------------------------
# DaSiamRPN
# Licensed under The MIT License
# Written by Qiang Wang (wangqiang2015 at ia.ac.cn)
# --------------------------------------------------------

import sys
import cv2
import torch
import numpy as np
from os.path import realpath, dirname, join

from net import SiamRPNBIG
from run_SiamRPN import SiamRPN_init, SiamRPN_track
from utils import get_axis_aligned_bbox, cxy_wh_2_rect, rect_2_cxy_wh


# custom modules to improve equirectangular tracking
from boundingbox import BoundingBox
from parser import Parser



class Tracker360Default:

    def __init__(self, video_path: str, groundtruth_path: str = None, save_result_path: str = None):
        self.video_path = video_path
        self.groundtruth_path = groundtruth_path
        if save_result_path:
            self.save_result_path = save_result_path
        else:    
            self.save_result_path = "tmp-result-DaSiamRPN.txt"

        self.net = None
        
        self.video = None
        self.video_width = None
        self.video_height = None
        self.frame = None
        self.tracker = None
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

        self.WINDOW_NAME = "Tracker-DaSiamRPN"


    # check if given point is in interval [0,self.width] and [0,self.height]
    def _checkBoundsOfPoint(self, point):
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


    # method for drawing rectangle according to points 
    def _drawBoundingBox(self, videoWidth, point1, point2, boundingBox, color, thickness):
        if (boundingBox.is_on_border()):
            # draw two rectangles around the region of interest
            rightBorderPoint = (videoWidth - 1, point2[1])
            cv2.rectangle(self.frame, point1, rightBorderPoint, color, thickness)

            leftBorderPoint = (0, point1[1])
            cv2.rectangle(self.frame, leftBorderPoint, point2, color, thickness)
        else:
            # draw a rectangle around the region of interest
            cv2.rectangle(self.frame, point1, point2, color, thickness)


    # method for saving result bounding boxes to txt file
    def _saveResults(self):
        # creating string result data
        resultData = self.parser.createAnnotations(self.result_bounding_boxes)
        # saving file on drive
        self.parser.saveDataToFile(self.save_result_path, resultData)
        print("File '" + self.save_result_path + "' has been successfully created with total " + str(len(self.result_bounding_boxes)) + " computed frames.")



    # method for start tracking without any modifications
    def run_video_default(self):
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


        ########## 2) Load pretrained model ##########
        # load net
        print("Loading pretrained model SiamRPNBIG.model...")
        self.net = SiamRPNBIG()
        self.net.load_state_dict(torch.load(join(realpath(dirname(__file__)), 'SiamRPNBIG.model')))
        self.net.eval().cuda()

        ########## 3) Setup opencv2 window ##########
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


        ########## 4) Initialation of bounding box ##########
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

            x, y, w, h = cv2.selectROI(self.WINDOW_NAME, frame_disp, fromCenter=False)
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


        ########## 5) Tracking process ##########
        # prints just basic guide and info
        print("--------------------------------------------------------------------")
        print("DaSiamRPN default tracking process has started...")
        print("Tracker  : DaSiamRPN")
        print("Frame #1 : " + str(self.bbox))
        print("Press 'Esc' or 'Q' key to exit")
        print("--------------------------------------------------------------------")

        # initialize tracker with first frame and bounding box
        ([cx, cy], [w, h]) = rect_2_cxy_wh(self.bbox)
        target_pos, target_sz = np.array([int(cx), int(cy)]), np.array([int(w), int(h)])
        state = SiamRPN_init(self.frame, target_pos, target_sz, self.net)

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

            # Get tracked bbox    
            state = SiamRPN_track(state, self.frame)  # track
            res = cxy_wh_2_rect(state['target_pos'], state['target_sz'])
            res = [int(l) for l in res]
            self.bbox = res

            # Calculate Frames per second (FPS)
            fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer)

            # draw bounding box
            if res[0] and res[1] and res[2] and res[3]:
                # Tracking success
                p1 = (res[0], res[1])
                p2 = (res[0] + res[2], res[1] + res[3])

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
            cv2.putText(self.frame, "DaSiamRPN Tracker", self.TEXT_ROW1_POS, cv2.FONT_HERSHEY_SIMPLEX, self.FONT_SCALE, (0, 200, 250), self.FONT_WEIGHT)
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
