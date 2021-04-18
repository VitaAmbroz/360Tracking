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

from boundingbox.boundingbox import BoundingBox


# TODO resizeWindow + correct circles, rectangles and text scaling when resizeWindow
# TODO add methods for computing selected metrics

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


    # method for running video and drawing groundtruth + result bounding boxes
    def runVideo(self):
        # Read video
        video = cv2.VideoCapture(self.path)
        # Exit if video not opened.
        if not video.isOpened():
            print("Error - Could not open video")
            sys.exit(-1)

        # Read first frame.
        ok, frame = video.read()
        if not ok:
            print("Error - Could not read a video file")
            sys.exit(-1)

        # store video width/height to variables
        videoWidth = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
        videoHeight = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))

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
        self._parseGivenDataFile(self.groundtruth_path, videoWidth, self.gt_bounding_boxes)
        self._parseGivenDataFile(self.result_path, videoWidth, self.result_bounding_boxes)

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

        
        # prints just basic guide and info
        print("----------------------------------------------------")
        print("This script shows groundtruth and also tracker results bounding boxes of particular objects for purpose of visual object tracking evaluation")
        print("Press 'Esc' or 'Q' key to exit")
        print("----------------------------------------------------")

        # FPS according to the original video
        fps = video.get(cv2.CAP_PROP_FPS)
        # fps = 30
        # calculate the interval between frame. 
        interval = int(1000/fps) 

        # counter of frames
        currentFrame = 0

        # Just read first frame for sure
        ok, frame = video.read()
        if not ok:
            print("Error - Could not read a video file")
            video.release()
            cv2.destroyAllWindows()
            sys.exit(-1)

        # keep looping until end of video, or until 'q' or 'Esc' key pressed
        while True:
            if currentFrame > 0:
                # Read a new frame
                ok, frame = video.read()
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
                        rightBorderPoint = (videoWidth - 1, pt2[1])
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
                        rightBorderPoint = (videoWidth - 1, pt2[1])
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
            cv2.putText(frame, ": " + self._bbString(gt_bb), self.TEXT_ROW2_POS2, cv2.FONT_HERSHEY_SIMPLEX, self.FONT_SCALE, (0, 250, 0), self.FONT_WEIGHT)
            cv2.putText(frame, "Tracker result (blue)", self.TEXT_ROW3_POS, cv2.FONT_HERSHEY_SIMPLEX, self.FONT_SCALE, (250, 0, 0), self.FONT_WEIGHT)
            cv2.putText(frame, ": " + self._bbString(res_bb), self.TEXT_ROW3_POS2, cv2.FONT_HERSHEY_SIMPLEX, self.FONT_SCALE, (250, 0, 0), self.FONT_WEIGHT)
            cv2.imshow(self.WINDOW_NAME, frame)
            
            # Exit if ESC or Q pressed
            k = cv2.waitKey(interval) & 0xff
            if k == 27 or k == ord('q'):
                break

        video.release()
        cv2.destroyAllWindows()


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
        self._parseGivenDataFile(self.groundtruth_path, videoWidth, self.gt_bounding_boxes)
        self._parseGivenDataFile(self.result_path, videoWidth, self.result_bounding_boxes)

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
        cv2.putText(images[currentFrame - 1], ": " + self._bbString(gt_bb), self.TEXT_ROW2_POS2, cv2.FONT_HERSHEY_SIMPLEX, self.FONT_SCALE, (0, 250, 0), self.FONT_WEIGHT)
        cv2.putText(images[currentFrame - 1], "Tracker result (blue)", self.TEXT_ROW3_POS, cv2.FONT_HERSHEY_SIMPLEX, self.FONT_SCALE, (250, 0, 0), self.FONT_WEIGHT)
        cv2.putText(images[currentFrame - 1], ": " + self._bbString(res_bb), self.TEXT_ROW3_POS2, cv2.FONT_HERSHEY_SIMPLEX, self.FONT_SCALE, (250, 0, 0), self.FONT_WEIGHT)
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
                cv2.putText(images[currentFrame - 1], ": " + self._bbString(gt_bb), self.TEXT_ROW2_POS2, cv2.FONT_HERSHEY_SIMPLEX, self.FONT_SCALE, (0, 250, 0), self.FONT_WEIGHT)
                cv2.putText(images[currentFrame - 1], "Tracker result (blue)", self.TEXT_ROW3_POS, cv2.FONT_HERSHEY_SIMPLEX, self.FONT_SCALE, (250, 0, 0), self.FONT_WEIGHT)
                cv2.putText(images[currentFrame - 1], ": " + self._bbString(res_bb), self.TEXT_ROW3_POS2, cv2.FONT_HERSHEY_SIMPLEX, self.FONT_SCALE, (250, 0, 0), self.FONT_WEIGHT)
                cv2.imshow(self.WINDOW_NAME, images[currentFrame - 1])
            # exit on 'ESC' or 'q' key
            elif key == 27  or key == ord('q'): 
                break

        cv2.destroyAllWindows()