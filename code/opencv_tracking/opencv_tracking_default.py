#################################################################################################
# Visual object tracking in panoramic video
# Master thesis at Brno University of Technology - Faculty of Information Technology
# Author:       Vít Ambrož (xambro15@stud.fit.vutbr.cz)
# Supervisor:   Doc. Ing. Martin Čadík, Ph.D.
# Module:       opencv_tracking_default.py
# Description:  Default tracking using OpenCV extra modules
#################################################################################################

from cv2 import cv2
import sys
import os

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from code.boundingbox import BoundingBox
from code.boundingbox import Parser
from code.nfov import NFOV

class OpenCVTrackingDefault:
    """Default tracking using OpenCV extra modules"""
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


    def _initLoad(self):
        """Method for video+groundtruth data loading and tracker initialization"""
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

        # save video width/height
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

        ########## 3) Setup opencv window ##########
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
            # using opencv select ROI
            cv2.putText(frame_disp, 'Select target ROI and press ENTER', self.TEXT_ROW1_POS, cv2.FONT_HERSHEY_SIMPLEX, self.FONT_SCALE, (0, 200, 250), self.FONT_WEIGHT)
            self.bbox = cv2.selectROI(self.WINDOW_NAME, frame_disp, False)

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


    def _saveResults(self):
        """Method for saving result bounding boxes to .txt file"""
        # creating string result data
        resultData = self.parser.createAnnotations(self.result_bounding_boxes)
        # saving file on drive
        self.parser.saveDataToFile(self.save_result_path, resultData)
        print("File '" + self.save_result_path + "' has been successfully created with total " + str(len(self.result_bounding_boxes)) + " computed frames.")


    def startTrackingDefault(self):
        """Method for start opencv tracking without any modifications"""
        # default load and init
        self._initLoad()

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
