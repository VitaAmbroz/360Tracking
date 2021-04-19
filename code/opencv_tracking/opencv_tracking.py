#################################################################################################
# Visual object tracking in panoramic video
# Master thesis at Brno University of Technology - Faculty of Information Technology
# Author:       Vít Ambrož (xambro15@stud.fit.vutbr.cz)
# Supervisor:   Doc. Ing. Martin Čadík, Ph.D.
# Module:       opencv_tracking.py
# Description:  Custom modifictaions of tracking for OpenCV extra modules
#################################################################################################

# import the necessary packages
from cv2 import cv2
import sys
import os
import glob
import numpy as np

from boundingbox.boundingbox import BoundingBox


class OpenCVTracking:
    def __init__(self, trackerName: str, videoPath: str, groundtruthPath: str, saveResultPath: str):
        self.tracker_name = trackerName.upper() # kcf -> KCF
        self.video_path = videoPath
        self.groundtruth_path = groundtruthPath
        self.save_result_path = saveResultPath

        self.video = None
        self.video_width = None
        self.video_height = None
        self.frame = None
        self.tracker = None
        self.bbox = None
        self.gt_bounding_boxes = []
        self.result_bounding_boxes = []
        self.current_frame = 1

        # constants for sizes and positions of opencv circles, rectangles and texts
        self.RECTANGLE_BORDER_PX = 2
        self.FONT_SCALE = 0.75
        self.FONT_WEIGHT = 2
        self.TEXT_ROW1_POS = (30,30)
        self.TEXT_ROW2_POS = (30,60)
        self.TEXT_ROW3_POS = (30,90)
        self.TEXT_ROW4_POS = (30,120)

        
        self.TRACKER_TYPES = ['BOOSTING', 'MIL', 'KCF', 'TLD', 'MEDIANFLOW', 'GOTURN', 'MOSSE', 'CSRT']

        self.WINDOW_NAME = "OpenCV-Tracker-" + self.tracker_name 

        self.WINDOW_NAME_BORDER = "OpenCV-Tracker-" + self.tracker_name + "-frame_shifted"


    # method for parsing ground truth data / result data from given filepath
    def _parseGivenDataFile(self, path, videoWidth, boundingBoxes):
        dataFile = open(path, 'r')
        lines = dataFile.readlines()

        for line in lines:
            # split line by comma char
            line_arr = line.split(',')

            if (line_arr[1] != 'nan' and line_arr[2] != 'nan' and line_arr[3] != 'nan' and line_arr[4] != 'nan'):
                x1 = int(line_arr[1])
                y1 = int(line_arr[2])
                # point 2 could be normalized because of border problem
                x2 = int(line_arr[1]) + int(line_arr[3])
                y2 = int(line_arr[2]) + int(line_arr[4])
                if x2 > videoWidth:
                    x2 = x2 - videoWidth

                bb = BoundingBox((x1, y1), (x2, y2), videoWidth)
                bb.is_annotated = True
                # save bounding box to bb list
                boundingBoxes.append(bb)
            else:
                bb = BoundingBox(None, None, videoWidth)
                bb.is_annotated = False
                # save unannotated bounding box to bb list
                boundingBoxes.append(bb)

    
    # method for creating string representing all annotated data (bounding_boxes list)
    def _createResult(self, boundingBoxesList):
        groundTruthResult = ""
        # loop in bounding_boxes list
        for idx in range(len(boundingBoxesList)):
            bb = boundingBoxesList[idx]
            groundTruthResult += self._createResultFrame(idx + 1, bb)
        return groundTruthResult


    # method for creating string representing annotated data of one frame
    def _createResultFrame(self, currentFrame, bb):
        groundTruthFrame = ""
        if bb and bb.is_annotated:
            groundTruthFrame += str(currentFrame) + ","
            groundTruthFrame += str(bb.get_x1()) + ","
            groundTruthFrame += str(bb.get_y1()) + ","
            groundTruthFrame += str(bb.get_width()) + ","
            groundTruthFrame += str(bb.get_height()) + "\n"
        else:
            groundTruthFrame += str(currentFrame) + ",nan,nan,nan,nan\n"
        return groundTruthFrame


    # method for creating file and writing data (overwrite file if already exists)
    def _saveResultToFile(self, path, data):
        newFile = open(path, "w")
        newFile.write(data)
        newFile.close()


    # method for creating string representation of annotated bounding box
    def _bbString(self, bb):
        groundTruthFrame = ""
        if bb and bb.is_annotated:
            groundTruthFrame += str(bb.get_x1()) + ","
            groundTruthFrame += str(bb.get_y1()) + ","
            groundTruthFrame += str(bb.get_width()) + ","
            groundTruthFrame += str(bb.get_height())
        else:
            groundTruthFrame += "nan,nan,nan,nan"
        return groundTruthFrame


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


    # method for loading video and groundtruth data, init tracker (the same start for all modifiations)
    def initLoad(self):
        ########## 1) Video Checking ##########
        # Read video
        self.video = cv2.VideoCapture(self.video_path)
        # Exit if video not opened.
        if not self.video.isOpened():
            print("Could not open video")
            print(help)
            sys.exit()

        # Read first frame.
        ok, self.frame = self.video.read()
        if not ok:
            print("Error - Could not read a video file")
            sys.exit()

        # save video width/height to global variables
        self.video_width = int(self.video.get(cv2.CAP_PROP_FRAME_WIDTH))
        self.video_height = int(self.video.get(cv2.CAP_PROP_FRAME_HEIGHT))

        ########## 2) Tracker Checking ##########
        # handle selection of tracker type
        if not(self.tracker_name in self.TRACKER_TYPES):
            print("Invalid tracker name: '" + self.tracker_name + "'")
            print("Supported tracker names: BOOSTING, MIL, KCF, TLD, MEDIANFLOW, GOTURN, MOSSE, CSRT")
            sys.exit()

        # Set up tracker
        if self.tracker_name == 'BOOSTING':
            self.tracker = cv2.TrackerBoosting_create()
        elif self.tracker_name == 'MIL':
            self.tracker = cv2.TrackerMIL_create()
        elif self.tracker_name == 'KCF':
            self.tracker = cv2.TrackerKCF_create()
        elif self.tracker_name == 'TLD':
            self.tracker = cv2.TrackerTLD_create()
        elif self.tracker_name == 'MEDIANFLOW':
            self.tracker = cv2.TrackerMedianFlow_create()
        elif self.tracker_name == 'GOTURN':
            self.tracker = cv2.TrackerGOTURN_create()
        elif self.tracker_name == 'MOSSE':
            self.tracker = cv2.TrackerMOSSE_create()
        elif self.tracker_name == 'CSRT':
            self.tracker = cv2.TrackerCSRT_create()


        ########## 3) Initialation of bounding box ##########
        # Set up initial bounding box
        self.bbox = None
        if self.groundtruth_path:
            # use first bounding box from given groundtruth
            self.boundingBoxes = []
            self._parseGivenDataFile(self.groundtruth_path, self.video_width, self.gt_bounding_boxes)
            
            if len(self.gt_bounding_boxes) > 0:
                bb1 = self.gt_bounding_boxes[0]
                if bb1.is_annotated:
                    self.bbox = (bb1.get_point1_x(), bb1.get_point1_y(), bb1.get_width(), bb1.get_height())
                    self.result_bounding_boxes.append(self.bbox)
                else:
                    print("Error - Invalid first frame annotation from file: '" + self.groundtruth_path + "'")
                    sys.exit()
        else:
            # TODO resize select ROI?
            # using opencv select ROI
            self.bbox = cv2.selectROI(self.frame, False)

        if not(self.bbox) or self.bbox == (0,0,0,0):
            print("Error - Invalid first frame annotation")
            sys.exit()

        print("Frame #1 : " + str(self.bbox))

        
        ########## 4) Setup opencv window ##########
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


    # method for start opencv tracking without any modifications
    def startTrackingDefault(self):
        # display first frame
        cv2.imshow(self.WINDOW_NAME, self.frame)

        # Initialize tracker with first frame and bounding box
        ok = self.tracker.init(self.frame, self.bbox)

        # if you want to have the FPS according to the video then uncomment this code
        # fps = cap.get(cv2.CAP_PROP_FPS)
        videoFPS = 30
        # calculate the interval between frame
        interval = int(1000/videoFPS) 

        # counter for frames
        self.current_frame = 1

        while True:
            # Read a new frame
            ok, self.frame = self.video.read()
            if not ok:
                break
            # increment counter
            self.current_frame += 1

            # Start timer
            timer = cv2.getTickCount()
            
            # Update tracker
            ok, self.bbox = self.tracker.update(self.frame)

            # Calculate Frames per second (FPS)
            fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer)

            # Draw bounding box
            if ok:
                # Tracking success
                p1 = (int(self.bbox[0]), int(self.bbox[1]))
                p2 = (int(self.bbox[0] + self.bbox[2]), int(self.bbox[1] + self.bbox[3]))
                cv2.rectangle(self.frame, p1, p2, (255,0,0), self.RECTANGLE_BORDER_PX, 1)

                # new instance of bounding box
                bb = BoundingBox(p1, p2, self.video_width)
                bb.is_annotated = True
                self.result_bounding_boxes.append(bb)
                
                dbgPrint = self._createResultFrame(self.current_frame, bb)
                print("Frame #" + str(self.current_frame) + " : " + dbgPrint[:-1])
            else:
                # Tracking failure
                cv2.putText(self.frame, "Tracking failure detected", self.TEXT_ROW4_POS, cv2.FONT_HERSHEY_SIMPLEX, self.FONT_SCALE, (0, 0, 255), self.FONT_WEIGHT)
                
                # new instance of bounding box
                bb = BoundingBox(None, None, self.video_width)
                bb.is_annotated = False
                self.result_bounding_boxes.append(bb)

                dbgPrint = self._createResultFrame(self.current_frame, bb)
                print("Frame #" + str(self.current_frame) + " : " + dbgPrint[:-1])

            # Display tracker type on frame
            cv2.putText(self.frame, self.tracker_name + " Tracker", self.TEXT_ROW1_POS, cv2.FONT_HERSHEY_SIMPLEX, self.FONT_SCALE, (0, 200, 250), self.FONT_WEIGHT)
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
            if k == 27: 
                break
        
        
        # creating string result data
        resultData = self._createResult(self.result_bounding_boxes)
        # TODO name
        name = "result-" + self.tracker_name + ".txt"
        # saving file on drive
        self._saveResultToFile(name, resultData)
        print("File '" + name + "' has been successfully created with total " + str(len(self.result_bounding_boxes)) + " computed frames.")

        self.video.release()
        cv2.destroyAllWindows()


    # method for start opencv tracking with improvement of object crossing left/right border in equirectangular projection
    def startTrackingBorder(self):
        # resize window for shifting (lets define max width is 1600px)
        if self.video_width < 1600:
            cv2.namedWindow(self.WINDOW_NAME_BORDER)
        else:
            cv2.namedWindow(self.WINDOW_NAME_BORDER, cv2.WINDOW_NORMAL | cv2.WINDOW_KEEPRATIO)
            whRatio = self.video_width / self.video_height
            if whRatio == 2:
                # pure equirectangular 2:1
                cv2.resizeWindow(self.WINDOW_NAME_BORDER, 1600, 800)
            else:
                # default 16:9
                cv2.resizeWindow(self.WINDOW_NAME_BORDER, 1600, 900)

        # display first frame
        cv2.imshow(self.WINDOW_NAME, self.frame)
        frameShifted = self.frame
        cv2.imshow(self.WINDOW_NAME_BORDER, frameShifted)

        # Initialize tracker with first frame and bounding box
        ok = self.tracker.init(self.frame, self.bbox)

        # if you want to have the FPS according to the video then uncomment this code
        # fps = cap.get(cv2.CAP_PROP_FPS)
        videoFPS = 30
        # calculate the interval between frame
        interval = int(1000/videoFPS) 

        # counter for frames
        self.current_frame = 1

        shiftLeftSlowly = 0
        shiftRightSlowly = 0
        p1 = (int(self.bbox[0]), int(self.bbox[1]))
        p2 = (int(self.bbox[0] + self.bbox[2]), int(self.bbox[1] + self.bbox[3]))
        
        while True:
            # Read a new frame
            ok, self.frame = self.video.read()
            if not ok:
                break
            # increment counter
            self.current_frame += 1
            # save reference
            frameShifted = self.frame

            if p1 and p2:
                # empiric constant = 1/8 of videoWidth is supposed to be good to start handle border translation
                if p1[0] < (self.video_width / 8):
                    # shift video_width / 100
                    shiftLeftSlowly += int(self.video_width / 100)
                    shiftLeftSlowly = shiftLeftSlowly % self.video_width
                elif p2[0] > self.video_width - (self.video_width / 8):
                    # shift video_width / 100
                    shiftRightSlowly += int(self.video_width / 100)
                    shiftRightSlowly = shiftRightSlowly % self.video_width
                
            if shiftLeftSlowly > 0 or shiftRightSlowly > 0:
                # shape of original frame
                rows,cols,_ = self.frame.shape
                dstLeftPart = None
                dstRightPart = None

                if shiftLeftSlowly > 0:
                    # shift to left
                    M1 = np.float32([[1,0,shiftLeftSlowly-cols], [0,1,0]])
                    dstLeftPart = cv2.warpAffine(self.frame, M1, (shiftLeftSlowly, rows))

                    M2 = np.float32([[1,0,0], [0,1,0]])
                    dstRightPart = cv2.warpAffine(self.frame, M2, (cols-shiftLeftSlowly, rows))
                elif shiftRightSlowly > 0:
                    # shift to right
                    M1 = np.float32([[1,0,-shiftRightSlowly], [0,1,0]])
                    dstLeftPart = cv2.warpAffine(self.frame, M1, (cols-shiftRightSlowly, rows))
                    
                    M2 = np.float32([[1,0,0], [0,1,0]])
                    dstRightPart = cv2.warpAffine(self.frame, M2, (shiftRightSlowly, rows))
                    
                # provide shift
                frameShifted = np.concatenate((dstLeftPart, dstRightPart), axis=1)

            # Start timer
            timer = cv2.getTickCount()
            
            # Update tracker
            ok, self.bbox = self.tracker.update(frameShifted)

            # Calculate Frames per second (FPS)
            fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer)

            # Draw bounding box
            if ok:
                # Tracking success
                p1 = (int(self.bbox[0]), int(self.bbox[1]))
                p2 = (int(self.bbox[0] + self.bbox[2]), int(self.bbox[1] + self.bbox[3]))
                cv2.rectangle(frameShifted, p1, p2, (255, 255, 0), self.RECTANGLE_BORDER_PX, 1)

                # normalize horizontal shifting
                tmpPoint1 = p1
                tmpPoint2 = p2
                if shiftLeftSlowly > 0:
                    # normalize horizontal shifting left to original equirectangular frame 
                    x1 = tmpPoint1[0]
                    x1 -= shiftLeftSlowly
                    if x1 < 0:
                        x1 = ((self.video_width + x1) % self.video_width) - 1
                    tmpPoint1 = (x1, tmpPoint1[1])

                    x2 = tmpPoint2[0]
                    x2 -= shiftLeftSlowly
                    if x2 < 0:
                        x2 = ((self.video_width + x2) % self.video_width) - 1
                    tmpPoint2 = (x2, tmpPoint2[1])
                elif shiftRightSlowly > 0:
                    # normalize horizontal shifting right to original equirectangular frame 
                    x1 = tmpPoint1[0]
                    x1 += shiftRightSlowly
                    if x1 > self.video_width:
                        x1 = (x1 % self.video_width) - 1
                    tmpPoint1 = (x1, tmpPoint1[1])

                    x2 = tmpPoint2[0]
                    x2 += shiftRightSlowly
                    if x2 > self.video_width:
                        x2 = (x2 % self.video_width) - 1
                    tmpPoint2 = (x2, tmpPoint2[1])

                # new instance of bounding box
                bb = BoundingBox(tmpPoint1, tmpPoint2, self.video_width)
                bb.is_annotated = True
                self.result_bounding_boxes.append(bb)

                # draw bounding box to original fram
                self._drawBoundingBox(self.video_width, tmpPoint1, tmpPoint2, bb, (0, 255, 0), self.RECTANGLE_BORDER_PX)
                
                # debug print
                dbgPrint = self._createResultFrame(self.current_frame, bb)
                print("Frame #" + str(self.current_frame) + " : " + dbgPrint[:-1])
            else:
                # Tracking failure
                cv2.putText(self.frame, "Tracking failure detected", self.TEXT_ROW4_POS, cv2.FONT_HERSHEY_SIMPLEX, self.FONT_SCALE, (0, 200, 255), self.FONT_WEIGHT)
                
                # reinit points
                p1 = None
                p2 = None

                # new instance of bounding box
                bb = BoundingBox(None, None, self.video_width)
                bb.is_annotated = False
                self.result_bounding_boxes.append(bb)

                # debug print
                dbgPrint = self._createResultFrame(self.current_frame, bb)
                print("Frame #" + str(self.current_frame) + " : " + dbgPrint[:-1])

            # Display tracker type on frame
            cv2.putText(self.frame, self.tracker_name + " Tracker", self.TEXT_ROW1_POS, cv2.FONT_HERSHEY_SIMPLEX, self.FONT_SCALE, (0, 255, 0), self.FONT_WEIGHT)
            # Display FPS on frame
            cv2.putText(self.frame, "Video   FPS : " + str(videoFPS), self.TEXT_ROW2_POS, cv2.FONT_HERSHEY_SIMPLEX, self.FONT_SCALE, (0, 255, 0), self.FONT_WEIGHT)
            cv2.putText(self.frame, "Tracker FPS : " + str(int(fps)), self.TEXT_ROW3_POS, cv2.FONT_HERSHEY_SIMPLEX, self.FONT_SCALE, (0, 255, 0), self.FONT_WEIGHT)
            
            # Display result
            cv2.imshow(self.WINDOW_NAME, self.frame)
            cv2.imshow(self.WINDOW_NAME_BORDER, frameShifted)

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
        
        
        # creating string data 
        resultData = self._createResult(self.result_bounding_boxes)
        name = "result-" + self.tracker_name + ".txt"
        # saving file on drive
        self._saveResultToFile(name, resultData)
        print("File '" + name + "' has been successfully created with total " + str(len(self.result_bounding_boxes)) + " computed frames.")

        self.video.release()
        cv2.destroyAllWindows()


    def startTrackingRectilinear(self):
        print("start tracking rectilinear")


    def startTrackingCentering(self):
        print("start tracking centering")
