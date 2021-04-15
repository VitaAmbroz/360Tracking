#################################################################################################
# Visual object tracking in panoramic video
# Master thesis at Brno University of Technology - Faculty of Information Technology
# Author:       Vít Ambrož (xambro15@stud.fit.vutbr.cz)
# Supervisor:   Doc. Ing. Martin Čadík, Ph.D.
# Module:       draw_annotation.py
# Description:  Simple opencv drawing of annotated objects in video frames / images sequences
#################################################################################################

from cv2 import cv2
import sys
import glob
import os

# from code.boundingbox.boundingbox import BoundingBox
# from code.boundingbox import BoundingBox
from boundingbox.boundingbox import BoundingBox


# TODO resizeWindow + correct circles, rectangles and text scaling when resizeWindow

class DrawAnnotation:
    def __init__(self, directoryPath: str):
        # list of annotated bounding box objects
        self.bounding_boxes = []
        
        self.directory_path = directoryPath


    # method for parsing ground truth data from given filepath
    def _parseGivenGroundtruth(self, path, videoWidth):
        # Read and parse existing groundtruth file
        if not(os.path.exists(path)):
            print("Error - Could not read a groundtruth file")
            sys.exit(-1)

        groundtruthFile = open(path, 'r')
        lines = groundtruthFile.readlines()

        for line in lines:
            # split line by comma char
            line_arr = line.split(',')

            if (line_arr[1] != 'nan' and line_arr[2] != 'nan' and line_arr[3] != 'nan' and line_arr[4] != 'nan'):
                x1 = int(line_arr[1])
                y1 = int(line_arr[2])
                # point 2 could be normalized because of border problem
                x2 = int(line_arr[1]) + int(line_arr[3])
                y2 = int(int(line_arr[2]) + int(line_arr[4]))
                if x2 > videoWidth:
                    x2 = x2 - videoWidth

                bb = BoundingBox((x1, y1), (x2, y2), videoWidth)
                bb.is_annotated = True
                # save bounding box to bb list
                self.bounding_boxes.append(bb)
            else:
                bb = BoundingBox(None, None, videoWidth)
                bb.is_annotated = False
                # save unannotated bounding box to bb list
                self.bounding_boxes.append(bb)


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


    # method for processing and showing annotated video frames sequence
    def runVideo(self):
        if not(self.directory_path.endswith("/")):
            self.directory_path += "/"
        VIDEO_PATH = self.directory_path + '*.mp4'
        GT_PATH = self.directory_path + 'groundtruth.txt'

        filenames = glob.glob(VIDEO_PATH)
        if len(filenames) < 1:
            print("Error - No video found in directory:" + self.directory_path)
            sys.exit(-1)

        # Read video
        video = cv2.VideoCapture(filenames[0])
        # Exit if video not opened.
        if not video.isOpened():
            print("Could not open video")
            sys.exit(-1)

        # Read first frame.
        ok, frame = video.read()
        if not ok:
            print("Error - Could not read a video file")
            sys.exit(-1)

        # save video width/height to variables
        videoWidth = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
        # video_height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
        
        # parse given groundtruth file
        self._parseGivenGroundtruth(GT_PATH, videoWidth)

        # counter of frames
        currentFrame = 1

        # setup the mouse callback function
        cv2.namedWindow("VideoAnnotation")

        # handle first frame
        bb = self.bounding_boxes[currentFrame - 1]
        # show annotations
        if bb and bb.is_annotated:
            pt1 = bb.point1
            pt2 = bb.point2
            if (bb.is_on_border()):
                # draw two rectangles around the region of interest
                rightBorderPoint = (videoWidth - 1, pt2[1])
                cv2.rectangle(frame, pt1, rightBorderPoint, (0, 255, 0), 2)

                leftBorderPoint = (0, pt1[1])
                cv2.rectangle(frame, leftBorderPoint, pt2, (0, 255, 0), 2)
            else:
                # draw a rectangle around the region of interest
                cv2.rectangle(frame, pt1, pt2, (0, 255, 0), 2)
        
        # display first frame
        # print("Frame #" + str(currentFrame))
        cv2.putText(frame, "Frame #" + str(currentFrame), (20,30), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (250, 250, 0), 2)
        cv2.putText(frame, "Groundtruth : " + self._bbString(bb), (20,60), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 250, 0), 2)
        cv2.imshow("VideoAnnotation", frame)
        
        # prints just basic guide and info
        print("----------------------------------------------------")
        print("This script shows annotated bounding boxes of particular objects for purpose of visual object tracking evaluation")
        print("Press 'Esc' or 'Q' key to exit")
        print("----------------------------------------------------")

        # # if you want to have the FPS according to the video then uncomment this code
        # # fps = cap.get(cv2.CAP_PROP_FPS)
        fps = 30
        # calculate the interval between frame. 
        interval = int(1000/fps) 

        # keep looping until end of video, or until 'q' or 'Esq' key pressed
        while True:
            # Read a new frame
            ok, frame = video.read()
            if not ok:
                break

            currentFrame += 1

            # video might be longer than groundtruth annotations
            if currentFrame <= len(self.bounding_boxes):
                # handle new (annotated) frame
                bb = self.bounding_boxes[currentFrame - 1]
                # show annotations
                if bb and bb.is_annotated:
                    pt1 = bb.point1
                    pt2 = bb.point2
                    if (bb.is_on_border()):
                        # draw two rectangles around the region of interest
                        rightBorderPoint = (videoWidth - 1, pt2[1])
                        cv2.rectangle(frame, pt1, rightBorderPoint, (0, 255, 0), 2)

                        leftBorderPoint = (0, pt1[1])
                        cv2.rectangle(frame, leftBorderPoint, pt2, (0, 255, 0), 2)
                    else:
                        # draw a rectangle around the region of interest
                        cv2.rectangle(frame, pt1, pt2, (0, 255, 0), 2)

            # display (annotated) frame
            # print("Frame #" + str(currentFrame))
            cv2.putText(frame, "Frame #" + str(currentFrame), (20,30), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (250, 250, 0), 2)
            cv2.putText(frame, "Groundtruth : " + self._bbString(bb), (20,60), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 250, 0), 2)
            cv2.imshow("VideoAnnotation", frame)
            
            # Exit if ESC or Q pressed
            k = cv2.waitKey(interval) & 0xff
            if k == 27 or k == ord('q'):
                break

        video.release()
        cv2.destroyAllWindows()


    # method for processing and showing annotated images sequence
    def runImageSeq(self):
        if not(self.directory_path.endswith("/")):
            self.directory_path += "/"
        IMG_PATH = self.directory_path + 'img/' + '*.jpg'
        GT_PATH = self.directory_path + 'groundtruth.txt'

        # first read images
        print("Reading all images - it might takes few seconds...")
        filenames = glob.glob(IMG_PATH)
        filenames.sort()
        images = [cv2.imread(img) for img in filenames]

        videoWidth = 0
        if len(images) > 0:
            _, width, _ = images[0].shape
            videoWidth = width
            # parse given groundtruth file
            self._parseGivenGroundtruth(GT_PATH, videoWidth)
        else:
            print("Error - No images to show.")
            sys.exit(-1)

        # create window
        cv2.namedWindow("ImagesAnnotation")

        # counter of frames
        currentFrame = 1
        
        # handle first frame
        bb = self.bounding_boxes[currentFrame - 1]
        # show annotations
        if bb and bb.is_annotated:
            pt1 = bb.point1
            pt2 = bb.point2
            if (bb.is_on_border()):
                # draw two rectangles around the region of interest
                rightBorderPoint = (videoWidth - 1, pt2[1])
                cv2.rectangle(images[currentFrame - 1], pt1, rightBorderPoint, (0, 255, 0), 2)

                leftBorderPoint = (0, pt1[1])
                cv2.rectangle(images[currentFrame - 1], leftBorderPoint, pt2, (0, 255, 0), 2)
            else:
                # draw a rectangle around the region of interest
                cv2.rectangle(images[currentFrame - 1], pt1, pt2, (0, 255, 0), 2)
        
        # show first frame
        # print("Frame #" + str(currentFrame))
        cv2.putText(images[currentFrame - 1], "Frame #" + str(currentFrame) + " - Press 'Enter' or 'C' for next frame", (20,30), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (250, 250, 0), 2)
        cv2.putText(images[currentFrame - 1], "Groundtruth : " + self._bbString(bb), (20,60), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 250, 0), 2)
        cv2.imshow("ImagesAnnotation", images[currentFrame - 1])

        # prints just basic guide and info
        print("----------------------------------------------------")
        print("This script shows annotated bounding boxes of particular objects for purpose of visual object tracking evaluation")
        print("----------------------------------------------------")
        print("Press 'Enter' or 'C' key to continue on following frame")
        print("Press 'Esc' or 'Q' key to exit")
        print("----------------------------------------------------")

        # showing next frame with 'c' or 'Enter' key pressed (Exit if 'Esc' or 'q' key pressed)
        while True:
            if currentFrame >= len(images) - 1:
                # end on the last frame
                break

            # capture key press
            key = cv2.waitKey(1) & 0xff
            # if the 'c' or 'enter' key is pressed, continue to next frame (right)
            if key == ord("c") or key == 10 or key == 13:
                # show next frames
                currentFrame += 1
                # print("Frame #" + str(currentFrame))

                bb = self.bounding_boxes[currentFrame - 1]
                # show annotations
                if bb and bb.is_annotated:
                    pt1 = bb.point1
                    pt2 = bb.point2
                    if (bb.is_on_border()):
                        # draw two rectangles around the region of interest
                        rightBorderPoint = (videoWidth - 1, pt2[1])
                        cv2.rectangle(images[currentFrame - 1], pt1, rightBorderPoint, (0, 255, 0), 2)

                        leftBorderPoint = (0, pt1[1])
                        cv2.rectangle(images[currentFrame - 1], leftBorderPoint, pt2, (0, 255, 0), 2)
                    else:
                        # draw a rectangle around the region of interest
                        cv2.rectangle(images[currentFrame - 1], pt1, pt2, (0, 255, 0), 2)
                
                # show frame
                        
                cv2.putText(images[currentFrame - 1], "Frame #" + str(currentFrame) + " - Press 'Enter' or 'C' for next frame", (20,30), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (250, 250, 0), 2)
                cv2.putText(images[currentFrame - 1], "Groundtruth : " + self._bbString(bb), (20,60), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 250, 0), 2)
                cv2.imshow("ImagesAnnotation", images[currentFrame - 1])
            # exit on 'ESC' or 'q' key
            elif key == 27  or key == ord('q'): 
                break

        cv2.destroyAllWindows()
