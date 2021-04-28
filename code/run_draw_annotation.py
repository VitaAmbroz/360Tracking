#################################################################################################
# Visual object tracking in panoramic video
# Master thesis at Brno University of Technology - Faculty of Information Technology
# Author:       Vít Ambrož (xambro15@stud.fit.vutbr.cz)
# Supervisor:   Doc. Ing. Martin Čadík, Ph.D.
# Module:       draw_annotation.py
# Description:  Top level of simple opencv drawing of annotated objects in video frames / images sequences
#################################################################################################

import argparse
import os
import sys

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from code.annotation import DrawAnnotation

###############################################################
###############            MAIN              ##################
###############################################################
if __name__ == '__main__':
    # construct the argument parser and parse the arguments
    ap = argparse.ArgumentParser(description='Run annotated objects in frames from given dataset directory.')
    ap.add_argument("-dir", "--directory", type=str, required=False, help="Path to the dataset directory - containing groundtruth.txt, *.mp4 and *.jpg files.")
    ap.add_argument("-demo", "--demo", action='store_true', help="Path to the dataset-demo directory - annotation/dataset-demo/demo-annotation/.")
    ap.add_argument("-v", "--video", action='store_true', help="Reading video frame by frame")
    ap.add_argument("-img", "--img", action='store_true', help="Reading images sequence")
    args = vars(ap.parse_args())

    # get directory path from arguments
    directoryPath = args["directory"]
    if not(directoryPath) and args["demo"]:
        directoryPath = "annotation/dataset-demo/demo-annotation/"
    elif not(directoryPath):
        print("Directory path missing -> run_draw_annotation.py -help")
        sys.exit(-1)

    # create instance for drawing annotations
    drawAnnotation = DrawAnnotation(directoryPath)

    if args["img"]:
        # run drawing on images sequence
        drawAnnotation.runImageSeq()
    else:
        # run video (that is default, flag -v is there just for strict call)
        drawAnnotation.runVideo()
