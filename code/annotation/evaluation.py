#################################################################################################
# Visual object tracking in panoramic video
# Master thesis at Brno University of Technology - Faculty of Information Technology
# Author:       Vít Ambrož (xambro15@stud.fit.vutbr.cz)
# Supervisor:   Doc. Ing. Martin Čadík, Ph.D.
# Module:       evaluation.py
# Description:  Evaluation single object trackers in custom groundtruth dataset
#################################################################################################

from cv2 import cv2
import sys
import glob
import os

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from code.boundingbox import Parser
from code.boundingbox import BoundingBox
# from boundingbox.boundingbox import BoundingBox

class Evaluation:
    def __init__(self, path: str, groundtruthPath: str, resultPath: str):
        # list of annotated groundtruth bounding box objects
        self.gt_bounding_boxes = []
        # list of tracker result bounding boxes
        self.gt_bounding_boxes = []

        # path of video file or directory with *.jpg images 
        self.path = path
        # path of file with groundtruth data 
        self.groundtruth_path = groundtruthPath
        # path of file with groundtruth data 
        self.result_path = resultPath

        # enable parsing/creating methods 
        self.parser = Parser()

        self.video = None
        self.video_width = None
        self.video_height = None

        # constants for sizes and positions of opencv rectangles and texts
        self.RECTANGLE_BORDER_PX = 2
        self.FONT_SCALE = 0.75
        self.FONT_WEIGHT = 2
        self.TEXT_ROW1_POS = (20,30)
        self.TEXT_ROW2_POS = (20,60)
        self.TEXT_ROW2_POS2 = (280,60)
        self.TEXT_ROW3_POS = (20,90)
        self.TEXT_ROW3_POS2 = (280,90)

        self.WINDOW_NAME = "Evaluation"


    # method for loading video, groundtruth and result data
    def loadInit(self):
        # Read video
        self.video = cv2.VideoCapture(self.path)
        # Exit if video not opened.
        if not self.video.isOpened():
            print("Error - Could not open video")
            sys.exit(-1)

        # store video width/height to variables
        self.video_width = int(self.video.get(cv2.CAP_PROP_FRAME_WIDTH))
        self.video_height = int(self.video.get(cv2.CAP_PROP_FRAME_HEIGHT))

        # Read and parse existing groundtruth file
        if not(os.path.exists(self.groundtruth_path)):
            print("Error - Could not read a groundtruth file")
            sys.exit(-1)

        # Read and parse existing tracking result file
        if not(os.path.exists(self.result_path)):
            print("Error - Could not read a tracking result file")
            sys.exit(-1)

        # list of annotated bounding box objects
        self.gt_bounding_boxes = []
        # list of tracking result bounding box objects
        self.result_bounding_boxes = []

        # parsing groundtruth and result files
        self.gt_bounding_boxes = self.parser.parseGivenDataFile(self.groundtruth_path, self.video_width)
        self.result_bounding_boxes = self.parser.parseGivenDataFile(self.result_path, self.video_width)


    # method for computing IoU metric between groundtruth and result bounding boxes
    # Intersection over Union is an evaluation metric used to measure the accuracy of an object tracker/detector...
    def computeIntersectionOverUnion(self):
        if len(self.gt_bounding_boxes) == len(self.result_bounding_boxes):
            # loop in bounding_boxes lists
            for idx in range(len(self.gt_bounding_boxes)):
                gt_bbox = self.gt_bounding_boxes[idx]
                result_bbox = self.result_bounding_boxes[idx]

                iou = self.intersectionOverUnion(gt_bbox, result_bbox)
                print("Frame #" + str(idx+1) + " : " + str(iou))


    # inspired and modified from https://www.pyimagesearch.com/2016/11/07/intersection-over-union-iou-for-object-detection/
    def intersectionOverUnion(self, bboxA: BoundingBox, bboxB: BoundingBox):
        # check if there are coordinates of bounding boxes
        if bboxA.point1 and bboxA.point2 and bboxB.point1 and bboxB.point2:
            # determine the (x,y)-coordinates of the intersection rectangle
            left_top_x = max(bboxA.get_point1_x(), bboxB.get_point1_x())
            left_top_y = max(bboxA.get_point1_y(), bboxB.get_point1_y())

            # not using point2 directly for right_bottom 
            # because point1 could be on right border, and point2 could be on left border of image
            right_bottom_x = min(bboxA.get_point1_x() + bboxA.get_width(), bboxB.get_point1_x() + bboxB.get_width())
            right_bottom_y = min(bboxA.get_point1_y() + bboxA.get_height(), bboxB.get_point1_y() + bboxB.get_height())

            # compute the area of intersection rectangle (inc +1 because of zero indexing in pixels coordinates)
            intersection_area = max(0, right_bottom_x - left_top_x + 1) * max(0, right_bottom_y - left_top_y + 1)

            # compute the area of both the prediction and ground-truth rectangles
            bboxA_area = bboxA.get_width() * bboxA.get_height()
            bboxB_area = bboxB.get_width() * bboxB.get_height()

            # compute the intersection over union by taking the intersection area
            # and dividing it by the sum of result + ground-truth areas - the interesection area
            iou = intersection_area / float(bboxA_area + bboxB_area - intersection_area)

            # return the intersection over union value
            return iou
        elif not(bboxA.point1) and not(bboxA.point2) and not(bboxB.point1) and not(bboxB.point2):
            return 1.0
        else:
            return 0.0


    # method for running video and drawing groundtruth + result bounding boxes
    def runVideo(self):
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
            self.TEXT_ROW2_POS2 = (int(self.TEXT_ROW2_POS2[0] * scaleFactor), int(self.TEXT_ROW2_POS2[1] * scaleFactor))
            self.TEXT_ROW3_POS = (int(self.TEXT_ROW3_POS[0] * scaleFactor), int(self.TEXT_ROW3_POS[1] * scaleFactor))
            self.TEXT_ROW3_POS2 = (int(self.TEXT_ROW3_POS2[0] * scaleFactor), int(self.TEXT_ROW3_POS2[1] * scaleFactor))

        
        # prints just basic guide and info
        print("----------------------------------------------------")
        print("This script shows groundtruth and also tracker results bounding boxes of particular objects for purpose of visual object tracking evaluation")
        print("Press 'Esc' or 'Q' key to exit")
        print("----------------------------------------------------")

        # FPS according to the original video
        fps = self.video.get(cv2.CAP_PROP_FPS)
        # fps = 30
        # calculate the interval between frame. 
        interval = int(1000/fps) 

        # counter of frames
        currentFrame = 0

        # Just read first frame for sure
        ok, frame = self.video.read()
        if not ok:
            print("Error - Could not read a video file")
            self.video.release()
            cv2.destroyAllWindows()
            sys.exit(-1)

        # keep looping until end of video, or until 'q' or 'Esc' key pressed
        while True:
            if currentFrame > 0:
                # Read a new frame
                ok, frame = self.video.read()
                if not ok:
                    break

            # increment counter of frames
            currentFrame += 1

            # video might be longer than groundtruth annotations
            if currentFrame <= len(self.gt_bounding_boxes):
                gt_bb = self.gt_bounding_boxes[currentFrame - 1]
                # show annotations
                if gt_bb and gt_bb.is_annotated:
                    pt1 = gt_bb.point1
                    pt2 = gt_bb.point2
                    if (gt_bb.is_on_border()):
                        # draw two rectangles around the region of interest
                        rightBorderPoint = (self.video_width - 1, pt2[1])
                        cv2.rectangle(frame, pt1, rightBorderPoint, (0, 255, 0), self.RECTANGLE_BORDER_PX)

                        leftBorderPoint = (0, pt1[1])
                        cv2.rectangle(frame, leftBorderPoint, pt2, (0, 255, 0), self.RECTANGLE_BORDER_PX)
                    else:
                        # draw a rectangle around the region of interest
                        cv2.rectangle(frame, pt1, pt2, (0, 255, 0), self.RECTANGLE_BORDER_PX)

            if currentFrame <= len(self.result_bounding_boxes):
                res_bb = self.result_bounding_boxes[currentFrame - 1]
                # show annotations
                if res_bb and res_bb.is_annotated:
                    pt1 = res_bb.point1
                    pt2 = res_bb.point2
                    if (res_bb.is_on_border()):
                        # draw two rectangles around the region of interest
                        rightBorderPoint = (self.video_width - 1, pt2[1])
                        cv2.rectangle(frame, pt1, rightBorderPoint, (255, 0, 0), self.RECTANGLE_BORDER_PX)

                        leftBorderPoint = (0, pt1[1])
                        cv2.rectangle(frame, leftBorderPoint, pt2, (255, 0, 0), self.RECTANGLE_BORDER_PX)
                    else:
                        # draw a rectangle around the region of interest
                        cv2.rectangle(frame, pt1, pt2, (255, 0, 0), self.RECTANGLE_BORDER_PX)


            # display (annotated) frame
            # print("Frame #" + str(currentFrame))
            cv2.putText(frame, "Frame #" + str(currentFrame), (20,30), cv2.FONT_HERSHEY_SIMPLEX, self.FONT_SCALE, (250, 250, 0), self.FONT_WEIGHT)
            cv2.putText(frame, "Groundtruth (green)", self.TEXT_ROW2_POS, cv2.FONT_HERSHEY_SIMPLEX, self.FONT_SCALE, (0, 250, 0), self.FONT_WEIGHT)
            cv2.putText(frame, ": " + self.parser.bboxString(gt_bb), self.TEXT_ROW2_POS2, cv2.FONT_HERSHEY_SIMPLEX, self.FONT_SCALE, (0, 250, 0), self.FONT_WEIGHT)
            cv2.putText(frame, "Tracker result (blue)", self.TEXT_ROW3_POS, cv2.FONT_HERSHEY_SIMPLEX, self.FONT_SCALE, (250, 0, 0), self.FONT_WEIGHT)
            cv2.putText(frame, ": " + self.parser.bboxString(res_bb), self.TEXT_ROW3_POS2, cv2.FONT_HERSHEY_SIMPLEX, self.FONT_SCALE, (250, 0, 0), self.FONT_WEIGHT)
            cv2.imshow(self.WINDOW_NAME, frame)
            
            # Exit if ESC or Q pressed
            k = cv2.waitKey(interval) & 0xff
            if k == 27 or k == ord('q'):
                break

        self.video.release()
        cv2.destroyAllWindows()


    # TOREMOVE? - images sequence maybe not supported here
    # method for running images .jpg sequence and drawing groundtruth + result bounding boxes
    def runImageSeq(self):
        if not(self.path.endswith("/")):
            self.path += "/"
        IMG_PATH = self.path + '*.jpg'

        # first read images
        print("Reading all images - it might takes few seconds...")
        filenames = glob.glob(IMG_PATH)
        filenames.sort()
        images = [cv2.imread(img) for img in filenames]

        videoWidth = 0
        videoHeight = 0
        if len(images) > 0:
            height, width, _ = images[0].shape
            videoWidth = width
            videoHeight = height
        else:
            print("Error - No images to show.")
            sys.exit(-1)

        # Read and parse existing groundtruth file
        if not(os.path.exists(self.groundtruth_path)):
            print("Error - Could not read a groundtruth file")
            sys.exit(-1)

        # Read and parse existing tracking result file
        if not(os.path.exists(self.result_path)):
            print("Error - Could not read a tracking result file")
            sys.exit(-1)

        # resize window (lets define max width is 1600px)
        if videoWidth < 1600:
            cv2.namedWindow(self.WINDOW_NAME)
        else:
            cv2.namedWindow(self.WINDOW_NAME, cv2.WINDOW_NORMAL | cv2.WINDOW_KEEPRATIO)
            whRatio = videoWidth / videoHeight
            if whRatio == 2:
                # pure equirectangular 2:1
                cv2.resizeWindow(self.WINDOW_NAME, 1600, 800)
            else:
                # default 16:9
                cv2.resizeWindow(self.WINDOW_NAME, 1600, 900)

            scaleFactor = videoWidth / 1600
            self.RECTANGLE_BORDER_PX = int(self.RECTANGLE_BORDER_PX * scaleFactor)
            self.FONT_SCALE = self.FONT_SCALE * scaleFactor
            self.FONT_WEIGHT = int(self.FONT_WEIGHT * scaleFactor) + 1
            self.TEXT_ROW1_POS = (int(self.TEXT_ROW1_POS[0] * scaleFactor), int(self.TEXT_ROW1_POS[1] * scaleFactor))
            self.TEXT_ROW2_POS = (int(self.TEXT_ROW2_POS[0] * scaleFactor), int(self.TEXT_ROW2_POS[1] * scaleFactor))
            self.TEXT_ROW2_POS2 = (int(self.TEXT_ROW2_POS2[0] * scaleFactor), int(self.TEXT_ROW2_POS2[1] * scaleFactor))
            self.TEXT_ROW3_POS = (int(self.TEXT_ROW3_POS[0] * scaleFactor), int(self.TEXT_ROW3_POS[1] * scaleFactor))
            self.TEXT_ROW3_POS2 = (int(self.TEXT_ROW3_POS2[0] * scaleFactor), int(self.TEXT_ROW3_POS2[1] * scaleFactor))

        # list of annotated bounding box objects
        self.gt_bounding_boxes = []
        # list of tracking result bounding box objects
        self.result_bounding_boxes = []

        # parsing groundtruth and result files
        self.gt_bounding_boxes = self.parser.parseGivenDataFile(self.groundtruth_path, videoWidth)
        self.result_bounding_boxes = self.parser.parseGivenDataFile(self.result_path, videoWidth)

        # counter of frames
        currentFrame = 1

        # handle first frame
        gt_bb = None
        if len(self.gt_bounding_boxes) > 0:
            gt_bb = self.gt_bounding_boxes[currentFrame - 1]
            # show annotations
            if gt_bb and gt_bb.is_annotated:
                pt1 = gt_bb.point1
                pt2 = gt_bb.point2
                if (gt_bb.is_on_border()):
                    # draw two rectangles around the region of interest
                    rightBorderPoint = (videoWidth - 1, pt2[1])
                    cv2.rectangle(images[currentFrame - 1], pt1, rightBorderPoint, (0, 255, 0), self.RECTANGLE_BORDER_PX)

                    leftBorderPoint = (0, pt1[1])
                    cv2.rectangle(images[currentFrame - 1], leftBorderPoint, pt2, (0, 255, 0), self.RECTANGLE_BORDER_PX)
                else:
                    # draw a rectangle around the region of interest
                    cv2.rectangle(images[currentFrame - 1], pt1, pt2, (0, 255, 0), self.RECTANGLE_BORDER_PX)

        res_bb = None
        if len(self.result_bounding_boxes) > 0:
            res_bb = self.result_bounding_boxes[currentFrame - 1]
            # show annotations
            if res_bb and gt_bb.is_annotated:
                pt1 = res_bb.point1
                pt2 = res_bb.point2
                if (res_bb.is_on_border()):
                    # draw two rectangles around the region of interest
                    rightBorderPoint = (videoWidth - 1, pt2[1])
                    cv2.rectangle(images[currentFrame - 1], pt1, rightBorderPoint, (255, 0, 0), self.RECTANGLE_BORDER_PX)

                    leftBorderPoint = (0, pt1[1])
                    cv2.rectangle(images[currentFrame - 1], leftBorderPoint, pt2, (255, 0, 0), self.RECTANGLE_BORDER_PX)
                else:
                    # draw a rectangle around the region of interest
                    cv2.rectangle(images[currentFrame - 1], pt1, pt2, (255, 0, 0), self.RECTANGLE_BORDER_PX)

        # display first frame
        # print("Frame #" + str(currentFrame))
        cv2.putText(images[currentFrame - 1], "Frame #" + str(currentFrame), self.TEXT_ROW1_POS, cv2.FONT_HERSHEY_SIMPLEX, self.FONT_SCALE, (250, 250, 0), self.FONT_WEIGHT)
        cv2.putText(images[currentFrame - 1], "Groundtruth (green)", self.TEXT_ROW2_POS, cv2.FONT_HERSHEY_SIMPLEX, self.FONT_SCALE, (0, 250, 0), self.FONT_WEIGHT)
        cv2.putText(images[currentFrame - 1], ": " + self.parser.bboxString(gt_bb), self.TEXT_ROW2_POS2, cv2.FONT_HERSHEY_SIMPLEX, self.FONT_SCALE, (0, 250, 0), self.FONT_WEIGHT)
        cv2.putText(images[currentFrame - 1], "Tracker result (blue)", self.TEXT_ROW3_POS, cv2.FONT_HERSHEY_SIMPLEX, self.FONT_SCALE, (250, 0, 0), self.FONT_WEIGHT)
        cv2.putText(images[currentFrame - 1], ": " + self.parser.bboxString(res_bb), self.TEXT_ROW3_POS2, cv2.FONT_HERSHEY_SIMPLEX, self.FONT_SCALE, (250, 0, 0), self.FONT_WEIGHT)
        cv2.imshow(self.WINDOW_NAME, images[currentFrame - 1])

        # prints just basic guide and info
        print("----------------------------------------------------")
        print("This script shows groundtruth and also tracker results bounding boxes of particular objects for purpose of visual object tracking evaluation")
        print("----------------------------------------------------")
        print("Press 'Enter' or 'C' key to continue on following frame")
        print("Press 'Esc' or 'Q' key to exit")
        print("----------------------------------------------------")

        # keep looping until end of video, or until 'q' or 'Esc' key pressed
        while True:
            if currentFrame >= len(images) - 1:
                # end on the last frame
                break
            
            # capture key press
            key = cv2.waitKey(1) & 0xff
            # if the 'c' or 'enter' key is pressed, continue to next frame (right)
            if key == ord("c") or key == 10 or key == 13:
                # increment counter of frames
                currentFrame += 1

                # video might be longer than groundtruth annotations
                if currentFrame <= len(self.gt_bounding_boxes):
                    gt_bb = self.gt_bounding_boxes[currentFrame - 1]
                    # show annotations
                    if gt_bb and gt_bb.is_annotated:
                        pt1 = gt_bb.point1
                        pt2 = gt_bb.point2
                        if (gt_bb.is_on_border()):
                            # draw two rectangles around the region of interest
                            rightBorderPoint = (videoWidth - 1, pt2[1])
                            cv2.rectangle(images[currentFrame - 1], pt1, rightBorderPoint, (0, 255, 0), self.RECTANGLE_BORDER_PX)

                            leftBorderPoint = (0, pt1[1])
                            cv2.rectangle(images[currentFrame - 1], leftBorderPoint, pt2, (0, 255, 0), self.RECTANGLE_BORDER_PX)
                        else:
                            # draw a rectangle around the region of interest
                            cv2.rectangle(images[currentFrame - 1], pt1, pt2, (0, 255, 0), self.RECTANGLE_BORDER_PX)

                if currentFrame <= len(self.result_bounding_boxes):
                    res_bb = self.result_bounding_boxes[currentFrame - 1]
                    # show annotations
                    if res_bb and res_bb.is_annotated:
                        pt1 = res_bb.point1
                        pt2 = res_bb.point2
                        if (res_bb.is_on_border()):
                            # draw two rectangles around the region of interest
                            rightBorderPoint = (videoWidth - 1, pt2[1])
                            cv2.rectangle(images[currentFrame - 1], pt1, rightBorderPoint, (255, 0, 0), self.RECTANGLE_BORDER_PX)

                            leftBorderPoint = (0, pt1[1])
                            cv2.rectangle(images[currentFrame - 1], leftBorderPoint, pt2, (255, 0, 0), self.RECTANGLE_BORDER_PX)
                        else:
                            # draw a rectangle around the region of interest
                            cv2.rectangle(images[currentFrame - 1], pt1, pt2, (255, 0, 0), self.RECTANGLE_BORDER_PX)


                # display (annotated) frame
                # print("Frame #" + str(currentFrame))
                cv2.putText(images[currentFrame - 1], "Frame #" + str(currentFrame), self.TEXT_ROW1_POS, cv2.FONT_HERSHEY_SIMPLEX, self.FONT_SCALE, (250, 250, 0), self.FONT_WEIGHT)
                cv2.putText(images[currentFrame - 1], "Groundtruth (green)", self.TEXT_ROW2_POS, cv2.FONT_HERSHEY_SIMPLEX, self.FONT_SCALE, (0, 250, 0), self.FONT_WEIGHT)
                cv2.putText(images[currentFrame - 1], ": " + self.parser.bboxString(gt_bb), self.TEXT_ROW2_POS2, cv2.FONT_HERSHEY_SIMPLEX, self.FONT_SCALE, (0, 250, 0), self.FONT_WEIGHT)
                cv2.putText(images[currentFrame - 1], "Tracker result (blue)", self.TEXT_ROW3_POS, cv2.FONT_HERSHEY_SIMPLEX, self.FONT_SCALE, (250, 0, 0), self.FONT_WEIGHT)
                cv2.putText(images[currentFrame - 1], ": " + self.parser.bboxString(res_bb), self.TEXT_ROW3_POS2, cv2.FONT_HERSHEY_SIMPLEX, self.FONT_SCALE, (250, 0, 0), self.FONT_WEIGHT)
                cv2.imshow(self.WINDOW_NAME, images[currentFrame - 1])
            # exit on 'ESC' or 'q' key
            elif key == 27  or key == ord('q'): 
                break

        cv2.destroyAllWindows()