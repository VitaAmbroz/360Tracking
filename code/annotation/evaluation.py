#################################################################################################
# Visual object tracking in panoramic video
# Master thesis at Brno University of Technology - Faculty of Information Technology
# Author:       Vít Ambrož (xambro15@stud.fit.vutbr.cz)
# Supervisor:   Doc. Ing. Martin Čadík, Ph.D.
# Module:       evaluation.py
# Description:  Evaluation of single object trackers in custom groundtruth dataset.
#               Drawing groundtruth+result bounding boxes or computing metrics.
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

class Evaluation:
    """
    Evaluation of single object trackers in custom groundtruth dataset.
    Drawing groundtruth+result bounding boxes or computing metrics.
    """
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


    def loadInit(self):
        """Method for loading video, groundtruth and result data"""
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


    def computeIntersectionOverUnion(self):
        """
        Method for computing IoU metric between groundtruth and result bounding boxes
        Intersection over Union is an evaluation metric used to measure the accuracy/success of an object tracker/detector
        """
        if len(self.gt_bounding_boxes) == len(self.result_bounding_boxes):
            iou_string = ""
            # loop in bounding_boxes lists
            for idx in range(len(self.gt_bounding_boxes)):
                gt_bbox = self.gt_bounding_boxes[idx]
                result_bbox = self.result_bounding_boxes[idx]

                # check if ground truth is not nan (occlusion) -> ignore occluded frames
                if gt_bbox.point1 and gt_bbox.point2:
                    iou = self.intersectionOverUnion(gt_bbox, result_bbox)
                    # store iou results to list
                    iou_string += str(iou) + "\n"

            # saving file on drive
            saveFilePath = self.result_path.replace(".txt", "-iou.txt")
            newFile = open(saveFilePath, "w")
            newFile.write(iou_string)
            newFile.close()
            print("File '" + saveFilePath + "' has been created.")
        
        self.video.release()


    # inspired and modified from https://www.pyimagesearch.com/2016/11/07/intersection-over-union-iou-for-object-detection/
    def intersectionOverUnion(self, bboxA: BoundingBox, bboxB: BoundingBox):
        """Method for computing IoU metric between 2 given bounding boxes"""
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

            # possible fix because of previous float rounding - max iou is 1.0
            if iou > 1.0:
                iou = 1.0
            
            # return the intersection over union value
            return iou
        else:
            # tracker failures
            return 0.0


    # def computeCenterError(self):
    #     """
    #     Method for computing Location error metric between groundtruth and result bounding boxes centers
    #     Location error is an evaluation metric used to measure the accuracy of an object tracker/detector
    #     """

    #     if len(self.gt_bounding_boxes) == len(self.result_bounding_boxes):
    #         centor_error_list = []
    #         center_error_string = ""

    #         # loop in bounding_boxes lists
    #         for idx in range(len(self.gt_bounding_boxes)):
    #             gt_bbox = self.gt_bounding_boxes[idx]
    #             result_bbox = self.result_bounding_boxes[idx]

    #             # check if ground truth is not Nan (occlusion) -> ignore occluded frames
    #             if gt_bbox.point1 and gt_bbox.point2:
    #                 center_error = self.intersectionOverUnion(gt_bbox, result_bbox)
    #                 # debug prints
    #                 print("Frame #" + str(idx+1) + " : " + str(center_error))
    #                 # store iou results to list
    #                 # iou_string += str(center_error) + "\n"

    #         # saving file on drive
    #         # saveFilePath = self.result_path.replace(".txt", "-iou.txt")
    #         # newFile = open(saveFilePath, "w")
    #         # newFile.write(iou_string)
    #         # newFile.close()
    #         # print("File '" + saveFilePath + "' has been created.")
        
    #     self.video.release()


    # def centerError(self, bboxA: BoundingBox, bboxB: BoundingBox):
    #     if bboxA.point1 and bboxA.point2 and bboxB.point1 and bboxB.point2:
    #         # bboxA and bboxB have valid coordinates ()
            

    #         # possible fix because of previous float rounding - max iou is 1.0
    #         if center_error < 0:
    #             center_error = 0
            
    #         # return the intersection over union value
    #         return center_error
    #     else:

    #         return -1


    def runVideo(self):
        """Method for running video and drawing groundtruth + result bounding boxes"""
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
