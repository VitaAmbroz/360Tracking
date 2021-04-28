#################################################################################################
# Visual object tracking in panoramic video
# Master thesis at Brno University of Technology - Faculty of Information Technology
# Author:       Vít Ambrož (xambro15@stud.fit.vutbr.cz)
# Supervisor:   Doc. Ing. Martin Čadík, Ph.D.
# Module:       parser.py
# Description:  Methods for parsing/creating bounding box objects from/to arrays/files
#################################################################################################

import sys
import os

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from code.boundingbox import BoundingBox

class Parser:
    """Methods for parsing/creating bounding box objects from/to arrays/files"""

    def parseGivenDataFile(self, path, videoWidth):
        """Method for parsing ground truth data / result data from given filepath"""
        dataFile = open(path, 'r')
        lines = dataFile.readlines()

        # init bounding box list
        boundingBoxesList = []

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

                bbox = BoundingBox((x1, y1), (x2, y2), videoWidth)
                bbox.is_annotated = True
                # save bounding box to bb list
                boundingBoxesList.append(bbox)
            else:
                bbox = BoundingBox(None, None, videoWidth)
                bbox.is_annotated = False
                # save unannotated bounding box to bb list
                boundingBoxesList.append(bbox)

        return boundingBoxesList

    
    def createAnnotations(self, boundingBoxesList):
        """Method for creating string representing all annotated data (bounding_boxes list)"""
        annotations = ""
        # loop in bounding_boxes list
        for idx in range(len(boundingBoxesList)):
            bbox = boundingBoxesList[idx]
            annotations += self.createFrameAnnotation(idx + 1, bbox)
        return annotations


    def createFrameAnnotation(self, currentFrame, bbox):
        """Method for creating string representing annotated data of one frame"""
        frameAnnotation = ""
        if bbox and bbox.is_annotated:
            frameAnnotation += str(currentFrame) + ","
            frameAnnotation += str(bbox.get_x1()) + ","
            frameAnnotation += str(bbox.get_y1()) + ","
            frameAnnotation += str(bbox.get_width()) + ","
            frameAnnotation += str(bbox.get_height()) + "\n"
        else:
            frameAnnotation += str(currentFrame) + ",nan,nan,nan,nan\n"
        return frameAnnotation


    def saveDataToFile(self, path, data):
        """Method for creating file and writing data (overwrite file if already exists)"""
        newFile = open(path, "w")
        newFile.write(data)
        newFile.close()


    def bboxString(self, bbox):
        """Method for creating string representation of annotated bounding box"""
        bboxToString = ""
        if bbox and bbox.is_annotated:
            bboxToString += str(bbox.get_x1()) + ","
            bboxToString += str(bbox.get_y1()) + ","
            bboxToString += str(bbox.get_width()) + ","
            bboxToString += str(bbox.get_height())
        else:
            bboxToString += "nan,nan,nan,nan"
        return bboxToString
