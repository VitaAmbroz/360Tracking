#################################################################################################
# Visual object tracking in panoramic video
# Master thesis at Brno University of Technology - Faculty of Information Technology
# Author:       Vít Ambrož (xambro15@stud.fit.vutbr.cz)
# Supervisor:   Doc. Ing. Martin Čadík, Ph.D.
# Module:       run_annotation_tool.py
# Description:  Top level of simple tool for annotating objects in equirectangular videos
#################################################################################################

import argparse
import os
import sys

from annotation.annotation_tool import AnnotationTool

###############################################################
###############            MAIN              ##################
###############################################################
if __name__ == '__main__':
    # construct the argument parser and parse the arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-v", "--video", required=True, help="Path to the video")
    ap.add_argument("-gt", "--groundtruth", required=False, help="Existing file with groundtruth data, that could be updated")
    ap.add_argument("-s", "--save", action='store_true', help="Flag for saving video frames as .jpg images")
    args = vars(ap.parse_args())

    # create instance of annotation tool
    annotation_tool = AnnotationTool(args["video"], args["groundtruth"], args["save"])
    annotation_tool.start()