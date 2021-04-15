#################################################################################################
# Visual object tracking in panoramic video
# Master thesis at Brno University of Technology - Faculty of Information Technology
# Author:       Vít Ambrož (xambro15@stud.fit.vutbr.cz)
# Supervisor:   Doc. Ing. Martin Čadík, Ph.D.
# Module:       annotation_tool.py
# Description:  Simple tool for annotating objects in equirectangular videos
#################################################################################################

# import the necessary packages
from cv2 import cv2
import argparse
import sys
import os

from boundingbox.boundingbox import BoundingBox


class AnnotationTool:
    def __init__(self, videoPath: str, groundtruthPath: str, saveImages: bool):
        self.bounding_boxes = []    # list of annotated bounding box objects
        self.bounding_box = None    # current bounding box
        self.current_frame = 1      # counter of frames

        self.frame = None           # reference for opencv frame
        self.clone = None           # reference for opencv tmp frame
        
        self.prev_bounding_box_mode = False     # flag for toggling feature that previous bounding box could be shown
        self.help_text = True                   # flag for showing help text in top left corner of frame
        
        self.pt1 = None             # current left point
        self.pt2 = None             # current right point
        self.video_width = None     # global width of video frame
        self.video_height = None    # global height of video frame
        
        self.video_path = videoPath                 # path of video file 
        self.groundtruth_path = groundtruthPath     # path of file with groundtruth data 
        self.save_images = saveImages               # flag for saving frame as .jpg images

        self.GT_PATH = "groundtruth.txt"            # path for possible created groundtruth.txt file
        self.SEQ_IMAGES_PATH = "img"                # directory for possible frames saving      


    # method for parsing ground truth data from given filepath
    def _parseGivenGroundtruth(self, path: str):
        # Read and parse existing groundtruth file
        if not(os.path.exists(path)):
            print("Error - Could not read a groundtruth file")
            sys.exit()

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
                if x2 > self.video_width:
                    x2 = x2 - self.video_width

                bb = BoundingBox((x1, y1), (x2, y2), self.video_width)
                bb.is_annotated = True
                # save bounding box to global list
                self.bounding_boxes.append(bb)
            else:
                bb = BoundingBox(None, None, self.video_width)
                bb.is_annotated = False
                # save unannotated bounding box to global list
                self.bounding_boxes.append(bb)


    # method for creating string representing all annotated data (bounding_boxes list)
    def _createGroundTruth(self, boundingBoxesList):
        groundTruthResult = ""
        # loop in bounding_boxes list
        for idx in range(len(boundingBoxesList)):
            bb = boundingBoxesList[idx]
            groundTruthResult += self._createGroundTruthFrame(idx + 1, bb)
        return groundTruthResult


    # method for creating string representing annotated data of one frame
    def _createGroundTruthFrame(self, currentFrame: int, bb):
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
    def _saveGroundTruthToFile(self, path: str, data):
        newFile = open(path, "w")
        newFile.write(data)
        newFile.close()


    # method for drawing rectangle according to points 
    def _drawBoundingBox(self, point1, point2, boundingBox, color, thickness):
        if (boundingBox.is_on_border()):
            # draw two rectangles around the region of interest
            rightBorderPoint = (self.video_width - 1, point2[1])
            cv2.rectangle(self.frame, point1, rightBorderPoint, color, thickness)

            leftBorderPoint = (0, point1[1])
            cv2.rectangle(self.frame, leftBorderPoint, point2, color, thickness)
        else:
            # draw a rectangle around the region of interest
            cv2.rectangle(self.frame, point1, point2, color, thickness)


    # method for managing bounding_box objectg in bounding_boxes list
    def _handleCurrentFrame(self, frameClone):
        if self.bounding_box and self.pt1 and self.pt2:
            # current frame has been annotated
            self.bounding_box.is_annotated = True
            # debugging info about annotation process - usable for user
            dbg = self._createGroundTruthFrame(self.current_frame, self.bounding_box)
            print("Frame #" + str(self.current_frame) + " - Annotation OK: " + dbg[:-1])
        else:
            # current frame has not been annotated
            # new instance of bounding box
            self.bounding_box = BoundingBox(self.pt1, self.pt2, self.video_width)
            self.bounding_box.is_annotated = False
            # debugging info about annotation process - usable for user
            dbg = self._createGroundTruthFrame(self.current_frame, self.bounding_box)
            print("Frame #" + str(self.current_frame) + " - Annotation OK (Empty): " + dbg[:-1])

        # create copy of frame before drawing
        self.bounding_box.frame_copy = frameClone.copy()

        if (self.current_frame == (len(self.bounding_boxes) + 1)):
            # push current frame with bounding_box to array
            self.bounding_boxes.append(self.bounding_box)
        else:
            # update current frame with bounding_box in array
            self.bounding_boxes[self.current_frame - 1] = self.bounding_box


    # method for showing previous annotation
    def _showPreviousBoundingBox(self, duplicate = False):
        if self.prev_bounding_box_mode:
            if self.current_frame > 1:
                prev = self.bounding_boxes[self.current_frame - 2]
                if prev and prev.is_annotated:
                    self._drawBoundingBox(prev.point1, prev.point2, prev, (255, 0, 0), 2)


    # method for duplicating previous annotation
    def _duplicatePreviousBoundingBox(self):
        if self.current_frame > 1:
            prev = self.bounding_boxes[self.current_frame - 2]
            if prev and prev.is_annotated:
                self.bounding_box = prev
                self.pt1 = prev.point1
                self.pt2 = prev.point2


    # method for creating string representation of annotated bounding box
    def _bbString(self, bb):
        groundTruthFrame = ""
        if bb and bb.point1 and bb.point2:
            groundTruthFrame += str(bb.get_x1()) + ","
            groundTruthFrame += str(bb.get_y1()) + ","
            groundTruthFrame += str(bb.get_width()) + ","
            groundTruthFrame += str(bb.get_height())
        else:
            groundTruthFrame += "nan,nan,nan,nan"
        return groundTruthFrame
    

    # method for drawing help + annotations directly to frame
    def _textToFrame(self):
        if self.help_text:
            # show Frame #currect_frame : bounding_box
            annotation = "nan,nan,nan,nan"
            if self.bounding_box:
                annotation = self._bbString(self.bounding_box)
            elif self.pt1:
                annotation = str(self.pt1[0]) + "," + str(self.pt1[1]) + ",nan,nan"

            cv2.putText(self.frame, "Frame #" + str(self.current_frame) + " : " + annotation, (20,25), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (250, 250, 0), 1)

            # show control help
            info = "'Enter' = next frame, 'Backspace' = previous frame, 'Q' = quit, 'H' = hide this text"
            cv2.putText(self.frame, info, (20,50), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 150, 250), 1,)
            info2 = "'R' = reset annotation, 'P' = previous annotation, 'D' = duplicate previous annotation"
            cv2.putText(self.frame, info2, (20,75), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 150, 250), 1)


    # mouse event handler
    # source: https://www.pyimagesearch.com/2015/03/09/capturing-mouse-click-events-with-python-and-opencv/
    def _click_bounding_box(self, event, x, y, flags, param):
        # check to see if the left mouse button was released
        if event == cv2.EVENT_LBUTTONUP:
            self.frame = self.clone.copy()

            # record the ending (x, y) coordinates
            if not(self.pt1):
                self.pt1 = (x, y)
                cv2.circle(self.frame, self.pt1, radius=5, color=(0, 255, 0), thickness=-1)
            elif not(self.pt2):
                self.pt2 = (x, y)
                cv2.circle(self.frame, self.pt2, radius=5, color=(0, 255, 0), thickness=-1)
            
            if self.pt1 and self.pt2:
                # new instance of bounding box
                self.bounding_box = BoundingBox(self.pt1, self.pt2, self.video_width)
                # create copy of frame before drawing
                self.bounding_box.frame_copy = self.frame.copy()

                # circles as points
                cv2.circle(self.frame, self.pt1, radius=5, color=(0, 255, 0), thickness=-1)
                cv2.circle(self.frame, self.pt2, radius=5, color=(0, 255, 0), thickness=-1)
                # rectangle(s) as bounding box
                self._drawBoundingBox(self.pt1, self.pt2, self.bounding_box, (0, 255, 0), 2)
            
            # showing frame
            self._showPreviousBoundingBox()
            self._textToFrame()
            cv2.imshow("video", self.frame)


    #######################################################################
    # main method for starting annotation proccess
    def start(self):
        # read video
        video = cv2.VideoCapture(self.video_path)

        # exit if video not opened.
        if not video.isOpened():
            print("Error - Could not open video")
            sys.exit()

        # Read first frame.
        ok, self.frame = video.read()
        if not ok:
            print("Error - Could not read a video file")
            sys.exit()

        # save clone for reset possibility of first frame
        self.clone = self.frame.copy()

        # save video width/height to global variables
        self.video_width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
        self.video_height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))

        # check if there is groundtruth file given
        if self.groundtruth_path:
            self._parseGivenGroundtruth(self.groundtruth_path)

        # setup the mouse callback function
        if self.video_width < 1400:
            cv2.namedWindow("video")
        else:
            cv2.namedWindow("video", cv2.WINDOW_NORMAL | cv2.WINDOW_KEEPRATIO)
            whRatio = self.video_width / self.video_height
            if whRatio == 2:
                # pure equirectangular 2:1
                cv2.resizeWindow("video", 1600, 800)
            else:
                # default 16:9
                cv2.resizeWindow("video", 1600, 900)

        # TODO correct circles, rectangles and text scaling when resizeWindow

        cv2.setMouseCallback("video", self._click_bounding_box)
        
        # display first frame
        if not(self.groundtruth_path):
            self._textToFrame()
        cv2.imshow("video", self.frame)

        # prints guide of this annotation tool
        print("----------------------------------------------------")
        print("This script enables annotating bounding boxes of particular objects for purpose of visual object tracking evaluation")
        print("----------------------------------------------------")
        print("First click is top/bottom LEFT corner of bounding box")
        print("Second click is top/bottom RIGHT corner of bounding box")
        print("----------------------------------------------------")
        print("Press 'Enter' key for continue on following frame <=> save current bounding box and show next frame")
        print("Press 'Backspace' key for going on previous frame <=> save current bounding box and show previous frame")
        print("Press 'R' key for reset of current bounding box")
        print("Press 'P' key for showing previous annotation <=> just show previous bounding box")
        print("Press 'D' key for duplicate previous annotation")
        print("----------------------------------------------------")

        # keep folder structure for saving new files with images and groundtruth
        directory, _ = os.path.split(self.video_path) 

        if directory:
            self.GT_PATH = directory + "/groundtruth.txt"
            self.SEQ_IMAGES_PATH = directory + "/img"

        # create new directory if it does not exists 
        # (https://www.tutorialspoint.com/How-can-I-create-a-directory-if-it-does-not-exist-using-Python)
        if self.save_images and not(os.path.exists(self.SEQ_IMAGES_PATH)):
            os.mkdir(self.SEQ_IMAGES_PATH)

        # variable for checking how many frames has been read - usage when annotating existing groundtruth data
        lastReadFrame = 1

        if self.save_images: 
            # save first image 0001.jpg
            name = "0001.jpg"
            cv2.imwrite(os.path.join(self.SEQ_IMAGES_PATH, name), self.frame)

        # first frame from groundtruth file
        if self.groundtruth_path and len(self.bounding_boxes) > 0:
            self.bounding_box = self.bounding_boxes[self.current_frame - 1]
            if self.bounding_box and self.bounding_box.is_annotated:
                self.pt1 = self.bounding_box.point1
                self.pt2 = self.bounding_box.point2
                # circles as points
                cv2.circle(self.frame, self.pt1, radius=5, color=(0, 255, 0), thickness=-1)
                cv2.circle(self.frame, self.pt2, radius=5, color=(0, 255, 0), thickness=-1)
                # rectangle(s) as bounding box
                self._drawBoundingBox(self.pt1, self.pt2, self.bounding_box, (0, 255, 0), 2)
                # showing frame with rectangles
                self._textToFrame()
                cv2.imshow("video", self.frame)

        # print debug info
        print("Showing frame #" + str(self.current_frame) + "...")

        ###############################################################
        # annotatiton process <=> keep looping until the 'q' or 'Esc' key is pressed
        while True:
            key = cv2.waitKey(1) & 0xff

            # if the 'enter' key is pressed, continue to next frame (right)
            if key == 10 or key == 13:
                # logic for handling current frame
                self._handleCurrentFrame(self.clone)

                # reading new frame (that has been not read yet)
                if self.current_frame == len(self.bounding_boxes):       
                    # reinit points and bounding box
                    self.pt1 = None
                    self.pt2 = None
                    self.bounding_box = None

                    # read and show new frame
                    ok, self.frame = video.read()
                    if not ok:
                        break
                    self.clone = self.frame.copy()
                    
                    # increment current_frame counter
                    self.current_frame += 1  
                    # increment lastReadFrame counter
                    lastReadFrame += 1
                    
                    # save image sequence 0001.jpg, 0002.jpg, ..., 0010.jpg, ..., 0100.jpg, ..., 1000.jpg, ...  
                    if self.save_images: 
                        name = str(self.current_frame).zfill(4) + ".jpg"
                        cv2.imwrite(os.path.join(self.SEQ_IMAGES_PATH, name), self.frame)
                    
                    # show frame (optional showing previous bounding_box)
                    self._showPreviousBoundingBox()
                    self._textToFrame()
                    cv2.imshow("video", self.frame)
                # user navigates between first frame and last read frame
                elif self.current_frame < len(self.bounding_boxes):
                    # increment current_frame counter
                    self.current_frame += 1

                    # reinit points and bounding box
                    self.pt1 = None
                    self.pt2 = None
                    self.bounding_box = None
                
                    self.bounding_box = self.bounding_boxes[self.current_frame - 1]
                    if self.bounding_box:
                        # check if frame has been already read
                        if lastReadFrame < len(self.bounding_boxes) and self.current_frame > lastReadFrame:
                            # read and show new frame
                            ok, self.frame = video.read()
                            if not ok:
                                break
                            self.clone = self.frame.copy()
                            # increment lastReadFrame counter
                            lastReadFrame += 1
                            # save image sequence 0001.jpg, 0002.jpg, ..., 0010.jpg, ..., 0100.jpg, ..., 1000.jpg, ...  
                            if self.save_images: 
                                name = str(self.current_frame).zfill(4) + ".jpg"
                                cv2.imwrite(os.path.join(self.SEQ_IMAGES_PATH, name), self.frame)
                        else:
                            # use saved copy of frame
                            self.frame = self.bounding_box.frame_copy.copy()
                            self.clone = self.frame.copy()
                            
                        # show annotations
                        if self.bounding_box.is_annotated:
                            self.pt1 = self.bounding_box.point1
                            self.pt2 = self.bounding_box.point2
                            # circles as points
                            cv2.circle(self.frame, self.pt1, radius=5, color=(0, 255, 0), thickness=-1)
                            cv2.circle(self.frame, self.pt2, radius=5, color=(0, 255, 0), thickness=-1)
                            # rectangle(s) as bounding box
                            self._drawBoundingBox(self.pt1, self.pt2, self.bounding_box, (0, 255, 0), 2)
                        
                        # show frame (optional showing previous bounding_box)
                        self._showPreviousBoundingBox()
                        self._textToFrame()
                        cv2.imshow("video", self.frame)
                    else:
                        print("Unexpected error when showing next frame - annotation process failed")
                        break
                else:
                    print("Unexpected error when showing next frame - annotation process failed")
                    break

                # print debug info
                print("--------------------------")
                print("Showing frame #" + str(self.current_frame) + "...")

            # if the 'Backspace' key is pressed, back to previous frame (left)
            elif key == 8:
                if self.current_frame > 1:
                    # logic for handling current frame
                    self._handleCurrentFrame(self.clone)

                    # reinit points and bounding box
                    self.pt1 = None
                    self.pt2 = None
                    self.bounding_box = None

                # decrement current_frame counter
                self.current_frame -= 1

                if self.current_frame > 0:
                    self.bounding_box = self.bounding_boxes[self.current_frame - 1]
                    if self.bounding_box:
                        # use saved copy of frame
                        self.frame = self.bounding_box.frame_copy.copy()
                        self.clone = self.frame.copy()
                        # show annotations
                        if self.bounding_box.is_annotated:
                            self.pt1 = self.bounding_box.point1
                            self.pt2 = self.bounding_box.point2
                            # circles as points
                            cv2.circle(self.frame, self.pt1, radius=5, color=(0, 255, 0), thickness=-1)
                            cv2.circle(self.frame, self.pt2, radius=5, color=(0, 255, 0), thickness=-1)
                            # rectangle(s) as bounding box
                            self._drawBoundingBox(self.pt1, self.pt2, self.bounding_box, (0, 255, 0), 2)
                        
                        # show frame (optional showing previous bounding_box)
                        self._showPreviousBoundingBox()
                        self._textToFrame()
                        cv2.imshow("video", self.frame)
                        # print debug info
                        print("--------------------------")
                        print("Showing frame #" + str(self.current_frame) + "...")
                    else:
                        print("Unexpected error when showing next frame - annotation failed")
                        break
                else:
                    # situation when trying to go left when is currently on frame 1
                    self.current_frame = 1

            # 'R' as Reset
            elif key == ord("r"):
                # if the 'r' key is pressed, reset current bounding_box
                self.frame = self.clone.copy()
                self.pt1 = None
                self.pt2 = None
                self.bounding_box = None

                # show frame
                self._showPreviousBoundingBox()
                self._textToFrame()
                cv2.imshow("video", self.frame)

            # 'P' as Previous
            elif key == ord("p"):
                # if the 'p' key is pressed, show/hide previous annotation
                if self.prev_bounding_box_mode:
                    self.prev_bounding_box_mode = False
                    print("Showing previous frames turned off.")
                else:
                    self.prev_bounding_box_mode = True
                    print("Showing previous frames turned on.")

                self.frame = self.clone.copy()
                self._showPreviousBoundingBox()  
                if self.pt1 and self.pt2:
                    # circles as points
                    cv2.circle(self.frame, self.pt1, radius=5, color=(0, 255, 0), thickness=-1)
                    cv2.circle(self.frame, self.pt2, radius=5, color=(0, 255, 0), thickness=-1)
                    # rectangle(s) as bounding box
                    self._drawBoundingBox(self.pt1, self.pt2, self.bounding_box, (0, 255, 0), 2)

                # show frame          
                self._textToFrame()
                cv2.imshow("video", self.frame)

            # 'D' as Duplicate
            elif key == ord("d"):
                # if the 'd' key is pressed, duplicate annotation from last_frame (useful when object is not moving)
                self.frame = self.clone.copy()
                self._showPreviousBoundingBox()
                # init pt1, pt2 and bounding_box from previous frame
                self._duplicatePreviousBoundingBox()

                if self.pt1 and self.pt2:
                    # circles as points
                    cv2.circle(self.frame, self.pt1, radius=5, color=(0, 255, 0), thickness=-1)
                    cv2.circle(self.frame, self.pt2, radius=5, color=(0, 255, 0), thickness=-1)
                    # rectangle(s) as bounding box
                    self._drawBoundingBox(self.pt1, self.pt2, self.bounding_box, (0, 255, 0), 2)

                # show frame
                self._textToFrame()
                cv2.imshow("video", self.frame)
            
            # 'H' as Hide Help text
            elif key == ord("h"):
                # if the 'h' key is pressed, toggle showing help text
                self.frame = self.clone.copy()
                
                if self.help_text:
                    self.help_text = False
                else:
                    self.help_text = True

                # show frame
                self._showPreviousBoundingBox()
                self._textToFrame()
                cv2.imshow("video", self.frame)

            # 'Q' as Quit
            elif key == 27 or key == ord("q"):
                # 'Esc' or 'Q' key pressed -> Save and Exit
                break


        # saving process
        # check if file already exists
        if os.path.exists(self.GT_PATH):
            print("File '" + self.GT_PATH + "' already exists. Do you want to overwrite it? (Y/N)")

            # keep looping until the 'y' or 'n' key is pressed
            while True:
                key = cv2.waitKey(1) & 0xff
                if key == ord("y") or key == ord("z"):
                    # creating ground truth data from bounding_boxes array
                    groundTruthData = self._createGroundTruth(self.bounding_boxes)
                    # saving file on drive
                    self._saveGroundTruthToFile(self.GT_PATH, groundTruthData)
                    print("File groundtruth.txt has been successfully created with total " + str(len(self.bounding_boxes)) + " annotated frames.")
                    break
                elif key == ord("n") or key == 27:
                    # 'n' or 'Esc'
                    break
        else:
            # creating ground truth data from bounding_boxes array
            groundTruthData = self._createGroundTruth(self.bounding_boxes)
            # saving file on drive
            self._saveGroundTruthToFile(self.GT_PATH, groundTruthData)
            print("File groundtruth.txt has been successfully created with total " + str(len(self.bounding_boxes)) + " annotated frames.")

        # TODO mozna odebrat mouse callback?
        video.release()
        cv2.destroyAllWindows()