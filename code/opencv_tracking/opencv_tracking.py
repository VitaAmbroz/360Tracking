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

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

# from boundingbox.boundingbox import BoundingBox
from code.boundingbox import BoundingBox
from code.boundingbox import Parser
from code.nfov import NFOV

class OpenCVTracking:
    def __init__(self, trackerName: str, videoPath: str, groundtruthPath: str, saveResultPath: str):
        self.tracker_name = trackerName.upper() # kcf -> KCF
        self.video_path = videoPath
        self.groundtruth_path = groundtruthPath
        self.save_result_path = saveResultPath
        if saveResultPath:
            self.save_result_path = saveResultPath
        else:    
            self.save_result_path = "tmp-result-" + self.tracker_name + ".txt"

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

        
        self.TRACKER_TYPES = ['BOOSTING', 'MIL', 'KCF', 'TLD', 'MEDIANFLOW', 'GOTURN', 'MOSSE', 'CSRT']

        self.WINDOW_NAME = "OpenCV-Tracker-" + self.tracker_name 
        self.WINDOW_NAME_BORDER = "OpenCV-Tracker-" + self.tracker_name + "-frame_shifted"
        self.WINDOW_NAME_RECTILINEAR = "OpenCV-Tracker-" + self.tracker_name + "-frame_rectilinear"


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

    # check if given point is in interval [0,self.width] and [0,self.height]
    def _checkBoundsOfPointStrict(self, point):
        # no horizontal overflow
        x = point[0]
        y = point[1]
        if x < 0: 
            x = 0
        elif x > self.video_width - 1: 
            x = self.video_width - 1
        
        # vertical
        if y < 0: 
            y = 0
        elif y > self.video_height - 1:
            y = self.video_height - 1

        point = (x,y)
        return point


    # method for loading video and groundtruth data, init tracker (the same start for all modifiations)
    def initLoad(self):
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

        ########## 2) Tracker Checking ##########
        # handle selection of tracker type
        if not(self.tracker_name in self.TRACKER_TYPES):
            print("Invalid tracker name: '" + self.tracker_name + "'")
            print("Supported tracker names: BOOSTING, MIL, KCF, TLD, MEDIANFLOW, GOTURN, MOSSE, CSRT")
            sys.exit(-1)

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
        self.gt_bounding_boxes = []
        self.result_bounding_boxes = []
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
            # TODO resize select ROI?
            # using opencv select ROI
            self.bbox = cv2.selectROI(self.frame, False)

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
            self.TEXT_ROW4_POS = (int(self.TEXT_ROW4_POS[0] * scaleFactor), int(self.TEXT_ROW4_POS[1] * scaleFactor))


    # method for saving result bounding boxes to txt file
    def _saveResults(self):
        # creating string result data
        resultData = self.parser.createAnnotations(self.result_bounding_boxes)
        # saving file on drive
        self.parser.saveDataToFile(self.save_result_path, resultData)
        print("File '" + self.save_result_path + "' has been successfully created with total " + str(len(self.result_bounding_boxes)) + " computed frames.")


    # method for start opencv tracking without any modifications
    def startTrackingDefault(self):
        # prints just basic guide and info
        print("--------------------------------------------------------------------")
        print("OpenCV default tracking process has started...")
        print("Tracker  : " + self.tracker_name)
        print("Frame #1 : " + str(self.bbox))
        print("Press 'Esc' or 'Q' key to exit")
        print("--------------------------------------------------------------------")

        # display first frame
        cv2.imshow(self.WINDOW_NAME, self.frame)

        # Initialize tracker with first frame and bounding box
        ok = self.tracker.init(self.frame, self.bbox)

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
            
            # Update tracker
            ok, self.bbox = self.tracker.update(self.frame)

            # Calculate Frames per second (FPS)
            fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer)

            # Draw bounding box
            if ok:
                # Tracking success
                p1 = (int(self.bbox[0]), int(self.bbox[1]))
                p2 = (int(self.bbox[0] + self.bbox[2]), int(self.bbox[1] + self.bbox[3]))

                p1 = self._checkBoundsOfPoint(p1)
                p2 = self._checkBoundsOfPoint(p2)

                # new instance of bounding box
                bb = BoundingBox(p1, p2, self.video_width)
                bb.is_annotated = True
                self.result_bounding_boxes.append(bb)

                # draw bounding box to original frame
                self._drawBoundingBox(self.video_width, p1, p2, bb, (0, 255, 0), self.RECTANGLE_BORDER_PX)
            else:
                # Tracking failure
                cv2.putText(self.frame, "Tracking failure detected", self.TEXT_ROW4_POS, cv2.FONT_HERSHEY_SIMPLEX, self.FONT_SCALE, (0, 0, 255), self.FONT_WEIGHT)
                
                # new instance of bounding box
                bb = BoundingBox(None, None, self.video_width)
                bb.is_annotated = False
                self.result_bounding_boxes.append(bb)

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
            if k == 27 or k == ord("q"): 
                break
        
        # always save tracker result
        self._saveResults()

        self.video.release()
        cv2.destroyAllWindows()


    # method for start opencv tracking with improvement of object crossing left/right border in equirectangular projection
    def startTrackingBorder(self):
        # prints just basic guide and info
        print("--------------------------------------------------------------------")
        print("OpenCV tracking process with borders improvement has started...")
        print("Tracker  : " + self.tracker_name)
        print("Frame #1 : " + str(self.bbox))
        print("Press 'Esc' or 'Q' key to exit")
        print("--------------------------------------------------------------------")

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

        # empiric constants - setup by experiments
        SHIFT_SLOW_START = int(self.video_width / 5)
        SHIFT_FAST_START = int(self.video_width / 8)

        SHIFT_SLOW_STEP_PX = int(self.video_width / 300)
        SHIFT_FAST_STEP_PX = int(self.video_width / 100)

        shiftLeft = 0
        shiftRight = 0
        p1 = (int(self.bbox[0]), int(self.bbox[1]))
        p2 = (int(self.bbox[0] + self.bbox[2]), int(self.bbox[1] + self.bbox[3]))
        
        while True:
            # Read a new frame
            ok, self.frame = self.video.read()
            if not ok:
                break
            # save reference
            frameShifted = self.frame

            if p1 and p2:
                # empiric constant for slow/smooth transitioning = 1/5 of videoWidth is supposed to be good to start handle border translation
                if p1[0] < SHIFT_SLOW_START:
                    # check if there has been any previous shiftRight
                    if shiftRight > 1:
                        shiftRight -= SHIFT_SLOW_STEP_PX
                        if shiftRight < 0:
                            shiftRight = 0
                        shiftRight = shiftRight % self.video_width
                    else:
                        shiftLeft += SHIFT_SLOW_STEP_PX
                        shiftLeft = shiftLeft % self.video_width
                elif p2[0] > self.video_width - SHIFT_SLOW_START:
                    # check if there has been any previous shiftLeft
                    if shiftLeft > 1:
                        shiftLeft -= SHIFT_SLOW_STEP_PX
                        if shiftLeft < 0:
                            shiftLeft = 0
                        shiftLeft = shiftLeft % self.video_width
                    else:
                        shiftRight += SHIFT_SLOW_STEP_PX
                        shiftRight = shiftRight % self.video_width

                # empiric constant for faster transitioning = 1/8 of videoWidth is supposed to be good to start faster transition
                if p1[0] < SHIFT_FAST_START:# check if there has been any previous shiftRight
                    if shiftRight > 1:
                        shiftRight -= SHIFT_FAST_STEP_PX
                        if shiftRight < 0:
                            shiftRight = 0
                        shiftRight = shiftRight % self.video_width
                    else:
                        shiftLeft += SHIFT_FAST_STEP_PX
                        shiftLeft = shiftLeft % self.video_width
                elif p2[0] > self.video_width - SHIFT_FAST_START:
                    # check if there has been any previous shiftLeft
                    if shiftLeft > 1:
                        shiftLeft -= SHIFT_FAST_STEP_PX
                        if shiftLeft < 0:
                            shiftLeft = 0
                        shiftLeft = shiftLeft % self.video_width
                    else:
                        shiftRight += SHIFT_FAST_STEP_PX
                        shiftRight = shiftRight % self.video_width
                
            if shiftLeft > 0 or shiftRight > 0:
                # shape of original frame
                rows,cols,_ = self.frame.shape
                dstLeftPart = None
                dstRightPart = None

                if shiftLeft > 0:
                    # shift to left
                    M1 = np.float32([[1,0,shiftLeft-cols], [0,1,0]])
                    dstLeftPart = cv2.warpAffine(self.frame, M1, (shiftLeft, rows))

                    M2 = np.float32([[1,0,0], [0,1,0]])
                    dstRightPart = cv2.warpAffine(self.frame, M2, (cols-shiftLeft, rows))
                elif shiftRight > 0:
                    # shift to right
                    M1 = np.float32([[1,0,-shiftRight], [0,1,0]])
                    dstLeftPart = cv2.warpAffine(self.frame, M1, (cols-shiftRight, rows))
                    
                    M2 = np.float32([[1,0,0], [0,1,0]])
                    dstRightPart = cv2.warpAffine(self.frame, M2, (shiftRight, rows))
                    
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

                p1 = self._checkBoundsOfPointStrict(p1)
                p2 = self._checkBoundsOfPointStrict(p2)
                cv2.rectangle(frameShifted, p1, p2, (255, 255, 0), self.RECTANGLE_BORDER_PX, 1)

                # normalize horizontal shifting
                tmpPoint1 = p1
                tmpPoint2 = p2
                if shiftLeft > 0:
                    # normalize horizontal shifting left to original equirectangular frame 
                    x1 = tmpPoint1[0]
                    x1 -= shiftLeft
                    if x1 < 0:
                        x1 = ((self.video_width + x1) % self.video_width) - 1
                    tmpPoint1 = (x1, tmpPoint1[1])

                    x2 = tmpPoint2[0]
                    x2 -= shiftLeft
                    if x2 < 0:
                        x2 = ((self.video_width + x2) % self.video_width) - 1
                    tmpPoint2 = (x2, tmpPoint2[1])
                elif shiftRight > 0:
                    # normalize horizontal shifting right to original equirectangular frame 
                    x1 = tmpPoint1[0]
                    x1 += shiftRight
                    if x1 > self.video_width:
                        x1 = (x1 % self.video_width) - 1
                    tmpPoint1 = (x1, tmpPoint1[1])

                    x2 = tmpPoint2[0]
                    x2 += shiftRight
                    if x2 > self.video_width:
                        x2 = (x2 % self.video_width) - 1
                    tmpPoint2 = (x2, tmpPoint2[1])

                # new instance of bounding box
                bb = BoundingBox(tmpPoint1, tmpPoint2, self.video_width)
                bb.is_annotated = True
                self.result_bounding_boxes.append(bb)

                # draw bounding box to original frame
                self._drawBoundingBox(self.video_width, tmpPoint1, tmpPoint2, bb, (0, 255, 0), self.RECTANGLE_BORDER_PX)
            else:
                # Tracking failure
                cv2.putText(self.frame, "Tracking failure detected", self.TEXT_ROW4_POS, cv2.FONT_HERSHEY_SIMPLEX, self.FONT_SCALE, (0, 0, 255), self.FONT_WEIGHT)
                
                # reinit points
                p1 = None
                p2 = None

                # new instance of bounding box
                bb = BoundingBox(None, None, self.video_width)
                bb.is_annotated = False
                self.result_bounding_boxes.append(bb)

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
        
        # always save tracker result
        self._saveResults()

        self.video.release()
        cv2.destroyAllWindows()


    # method for start opencv tracking with improvement of mapping equirectangular to rectilinear projection
    def startTrackingNFOV(self):
        # prints just basic guide and info
        print("--------------------------------------------------------------------")
        print("OpenCV tracking process with rectilinear improvement has started...")
        print("Tracker  : " + self.tracker_name)
        print("Frame #1 : " + str(self.bbox))
        print("Press 'Esc' or 'Q' key to exit")
        print("--------------------------------------------------------------------")


        ##########################################################################
        ################## Normal field of view initialization ###################
        ##########################################################################
        # init instance for normal field of view according to rectilinear framework
        nfov_width = int(self.video_width / 2)
        nfov_height = int(self.video_height / 2)

        # lets define max rectilinear window size - 720p
        if nfov_width > 1440 or nfov_height > 720:
            whRatio = nfov_width / nfov_height
            nfov_height = 720
            nfov_width = round(whRatio * 720)

        # create instance of NFOV
        nfov = NFOV(nfov_height, nfov_width)

        # center point of selected bounding box
        center_equi_x = int(self.bbox[0] + self.bbox[2]/2)
        center_equi_y = int(self.bbox[1] + self.bbox[3]/2)
        center_equi_x_normalized = center_equi_x / self.video_width
        center_equi_y_normalized = center_equi_y / self.video_height
        
        # bounding box points left_top and bottom_right
        x1_normalized = self.bbox[0] / self.video_width
        y1_normalized = self.bbox[1] / self.video_height
        x2_normalized = (self.bbox[0] + self.bbox[2]) / self.video_width
        y2_normalized = (self.bbox[1] + self.bbox[3]) / self.video_height

        # camera center point (valid range [0,1])
        center_point = np.array([center_equi_x_normalized, center_equi_y_normalized])
        # bounding box points left_top and bottom_right
        nfov.point1_equi = np.array([x1_normalized, y1_normalized])
        nfov.point2_equi = np.array([x2_normalized, y2_normalized])
        # remap to normal field of view
        frameRectilinear = nfov.toNFOV(self.frame, center_point, computeRectPoints=True)

        # get coordinates of points in rectilinear projection
        x1_rect = int(nfov.point1_rect[0])
        y1_rect = int(nfov.point1_rect[1])
        width_rect = int(nfov.point2_rect[0] - nfov.point1_rect[0])
        height_rect = int(nfov.point2_rect[1] - nfov.point1_rect[1])


        ##########################################################################
        ################## Tracking process initialization #######################
        ##########################################################################
        # use bounding box representation also in rectilinear
        bbox_rect = (x1_rect, y1_rect, width_rect, height_rect)

        # top left in equirectangular
        p1_equi = (int(self.bbox[0]), int(self.bbox[1]))
        # bottom right in equirectangular
        p2_equi = (int(self.bbox[0] + self.bbox[2]), int(self.bbox[1] + self.bbox[3]))

        # top left in rectilinear
        p1_rect = (bbox_rect[0], bbox_rect[1])
        # bottom right in rectilinear
        p2_rect = (bbox_rect[0] + bbox_rect[2], bbox_rect[1] + bbox_rect[3])

        # display first frame
        cv2.rectangle(self.frame, p1_equi, p2_equi, (0, 255, 0), 2, 1)
        cv2.imshow(self.WINDOW_NAME, self.frame)

        cv2.namedWindow(self.WINDOW_NAME_RECTILINEAR)
        cv2.rectangle(frameRectilinear, p1_rect, p2_rect, (255, 255, 0), 2, 1)
        cv2.imshow(self.WINDOW_NAME_RECTILINEAR, frameRectilinear)

        # initialize tracker with first frame and bounding box
        ok = self.tracker.init(frameRectilinear, bbox_rect)

        # max fps
        videoFPS = 30
        # videoFPS = cap.get(cv2.CAP_PROP_FPS) 
        # calculate the interval between frame
        interval = int(1000/videoFPS) 

        # cv2.waitKey(0)

        # empiric constants for shifting/scaling in rectilinear projection - setup by experiments
        SHIFT_SLOW_X_START = 0.45 * nfov_width
        SHIFT_SLOW_Y_START = 0.45 * nfov_height
        SHIFT_FAST_X_START = 0.35 * nfov_width
        SHIFT_FAST_Y_START = 0.35 * nfov_height

        SHIFT_FAST_X = int(self.video_width / 100)
        SHIFT_FAST_Y = int(self.video_height / 100)

        SHIFT_SLOW_X = int(self.video_width / 200)
        SHIFT_SLOW_Y = int(self.video_height / 200)

        SCALEDOWN_FOV_SLOW_START_X = 0.66 * nfov_width
        SCALEDOWN_FOV_SLOW_START_Y = 0.66 * nfov_height

        SCALEDOWN_FOV_FAST_START_X = 0.8 * nfov_width
        SCALEDOWN_FOV_FAST_START_Y = 0.8 * nfov_height

        SCALEUP_FOV_SLOW_START_X = 0.33 * nfov_width
        SCALEUP_FOV_SLOW_START_Y = 0.33 * nfov_height
        
        SCALE_FOV_STEP_SLOW = 0.01
        SCALE_FOV_STEP_FAST = 0.02

        while True:
            # Read a new frame
            ok, self.frame = self.video.read()
            if not ok:
                break

            # Start timer
            timer = cv2.getTickCount()
            
            # update center point
            if p1_rect and p2_rect and bbox_rect:
                # center of bounding box in rectilinear projection
                center_rect = [bbox_rect[0] + bbox_rect[2]/2, bbox_rect[1] + bbox_rect[3]/2]

                # SHIFTS X
                # FAST
                if center_rect[0] < SHIFT_FAST_X_START:
                    center_equi_x -= SHIFT_FAST_X
                    if center_equi_x < 0:
                        center_equi_x = self.video_width + center_equi_x
                    else:
                        center_equi_x = center_equi_x % self.video_width
                elif center_rect[0] > nfov_width - SHIFT_FAST_X_START:
                    center_equi_x += SHIFT_FAST_X
                    center_equi_x = center_equi_x % self.video_width
                # SLOW
                elif center_rect[0] < SHIFT_SLOW_X_START:
                    center_equi_x -= SHIFT_SLOW_X
                    if center_equi_x < 0:
                        center_equi_x = self.video_width + center_equi_x
                    else:
                        center_equi_x = center_equi_x % self.video_width
                elif center_rect[0] > nfov_width - SHIFT_SLOW_X_START:
                    center_equi_x += SHIFT_SLOW_X
                    center_equi_x = center_equi_x % self.video_width
                

                # SHIFTS Y
                # FAST
                if center_rect[1] < SHIFT_FAST_Y_START:
                    center_equi_y -= SHIFT_FAST_Y
                    if center_equi_y < 0:
                        center_equi_y = self.video_height + center_equi_y
                    else:
                        center_equi_y = center_equi_y % self.video_height
                elif center_rect[1] > nfov_height - SHIFT_FAST_Y_START:
                    center_equi_y += SHIFT_FAST_Y
                    center_equi_y = center_equi_y % self.video_height
                # SLOW Y
                elif center_rect[1] < SHIFT_SLOW_Y_START:
                    center_equi_y -= SHIFT_SLOW_Y
                    if center_equi_y < 0:
                        center_equi_y = self.video_height + center_equi_y
                    else:
                        center_equi_y = center_equi_y % self.video_height
                elif center_rect[1] > nfov_height - SHIFT_SLOW_Y_START:
                    center_equi_y += SHIFT_SLOW_Y
                    center_equi_y = center_equi_y % self.video_height


                # default nfov.FOV is 0.5 == 90°
                # rescale FOV - enable zoom back (further from object)
                # object is close to camera/big -> increase field of view
                # FAST
                if bbox_rect[2] > SCALEDOWN_FOV_FAST_START_X or bbox_rect[3] > SCALEDOWN_FOV_FAST_START_Y:
                    # max FOV 0.8 == 144° 
                    if nfov.FOV[0] < 0.8:
                        nfov.FOV = [nfov.FOV[0] + SCALE_FOV_STEP_FAST, nfov.FOV[1] + SCALE_FOV_STEP_FAST]
                # SLOW
                elif bbox_rect[2] > SCALEDOWN_FOV_SLOW_START_X or bbox_rect[3] > SCALEDOWN_FOV_SLOW_START_Y:
                    # max FOV 0.8 == 144°
                    if nfov.FOV[0] < 0.8:
                        nfov.FOV = [nfov.FOV[0] + SCALE_FOV_STEP_SLOW, nfov.FOV[1] + SCALE_FOV_STEP_SLOW]
                # rescale FOV - enable zoom forward (closer from object)
                elif bbox_rect[2] < SCALEUP_FOV_SLOW_START_X and bbox_rect[3] < SCALEUP_FOV_SLOW_START_Y:
                    # object is small and field of view is large 
                    if nfov.FOV[0] > 0.6:
                        # decrease field of view
                        nfov.FOV = [nfov.FOV[0] - SCALE_FOV_STEP_SLOW, nfov.FOV[1] - SCALE_FOV_STEP_SLOW]

            # normalize center point in [0,1]
            center_equi_x_normalized = center_equi_x / self.video_width
            center_equi_y_normalized = center_equi_y / self.video_height
            # camera center point (valid range [0,1])
            center_point = np.array([center_equi_x_normalized, center_equi_y_normalized])  

            # new frame to rectilinear/normal field of view
            frameRectilinear = nfov.toNFOV(self.frame, center_point)

            # Update tracker
            ok, bbox_rect = self.tracker.update(frameRectilinear)

            # calculate Frames per second after tracking (FPS)
            fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer)

            # handle tracking result
            if ok:
                # rectilinear
                p1_rect = (int(round(bbox_rect[0])), int(round(bbox_rect[1])))
                p2_rect = (int(round(bbox_rect[0] + bbox_rect[2])), int(round(bbox_rect[1] + bbox_rect[3])))
                # store points to nfov instance
                nfov.point1_rect = [p1_rect[0], p1_rect[1]]
                nfov.point2_rect = [p2_rect[0], p2_rect[1]]
                # draw bounding box to rectilinear frame
                cv2.rectangle(frameRectilinear, p1_rect, p2_rect, (255, 255, 0), self.RECTANGLE_BORDER_PX, 1)

                # equirectangular
                # compute corresponding points of rectilinear bounding box in equirectangular projection 
                nfov.computeEquirectangularBbox(bbox_width=round(bbox_rect[2]), bbox_height=round(bbox_rect[3]))
                # bbox points top left and right bottom in equirectangular projection
                p1_equi = (int(round(nfov.point1_equi[0] * self.video_width)), int(round(nfov.point1_equi[1] * self.video_height)))
                p2_equi = (int(round(nfov.point2_equi[0] * self.video_width)), int(round(nfov.point2_equi[1] * self.video_height)))

                # in NFOV points.x could be negative
                p1_equi = self._checkBoundsOfPoint(p1_equi)
                p2_equi = self._checkBoundsOfPoint(p2_equi)

                # create custom equirectangular bounding box instance
                bb = BoundingBox(p1_equi, p2_equi, self.video_width)
                bb.is_annotated = True
                self.result_bounding_boxes.append(bb)

                # draw bounding box to original equirectangular frame
                self._drawBoundingBox(self.video_width, p1_equi, p2_equi, bb, (0, 255, 0), self.RECTANGLE_BORDER_PX)
            else:
                # tracking failure
                cv2.putText(self.frame, "Tracking failure detected", self.TEXT_ROW4_POS, cv2.FONT_HERSHEY_SIMPLEX, self.FONT_SCALE, (0, 0, 255), self.FONT_WEIGHT)
                
                # reinit points
                p1_rect = None
                p2_rect = None
                p1_equi = None
                p2_equi = None

                # create custom empty equirectangular bounding box instance
                bb = BoundingBox(None, None, self.video_width)
                bb.is_annotated = False
                self.result_bounding_boxes.append(bb)
            
            # Display tracker type on frame
            cv2.putText(self.frame, self.tracker_name + " Tracker", self.TEXT_ROW1_POS, cv2.FONT_HERSHEY_SIMPLEX, self.FONT_SCALE, (0, 255, 0), self.FONT_WEIGHT)
            # Display FPS on frame
            cv2.putText(self.frame, "Video   FPS : " + str(videoFPS), self.TEXT_ROW2_POS, cv2.FONT_HERSHEY_SIMPLEX, self.FONT_SCALE, (0, 255, 0), self.FONT_WEIGHT)
            cv2.putText(self.frame, "Tracker FPS : " + str(int(fps)), self.TEXT_ROW3_POS, cv2.FONT_HERSHEY_SIMPLEX, self.FONT_SCALE, (0, 255, 0), self.FONT_WEIGHT)
            
            # Display result
            cv2.imshow(self.WINDOW_NAME, self.frame)
            cv2.imshow(self.WINDOW_NAME_RECTILINEAR, frameRectilinear)


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
        
        # release, destroy
        self.video.release()
        cv2.destroyAllWindows()

