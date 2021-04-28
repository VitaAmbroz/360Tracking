#################################################################################################
# Visual object tracking in panoramic video
# Master thesis at Brno University of Technology - Faculty of Information Technology
# Author:       Vít Ambrož (xambro15@stud.fit.vutbr.cz)
# Supervisor:   Doc. Ing. Martin Čadík, Ph.D.
# Module:       run_opencv_tracking.py
# Description:  Top level module for running equirectangular improvements of OpenCV extra modules trackers
#################################################################################################

import argparse
import os
import sys

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from code.opencv_tracking import OpenCVTrackingDefault
from code.opencv_tracking import OpenCVTrackingBorder
from code.opencv_tracking import OpenCVTrackingNFOV

###############################################################
###############            MAIN              ##################
###############################################################
if __name__ == '__main__':
    # construct the argument parser and parse the arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-t", "--tracker", required=True, help="OpenCV tracker name - 'BOOSTING', 'MIL', 'KCF', 'TLD', 'MEDIANFLOW', 'GOTURN', 'MOSSE', 'CSRT'")
    ap.add_argument("-v", "--video", required=True, help="Path to the video")
    ap.add_argument("-gt", "--groundtruth", required=False, help="Path to the file with groundtruth data (Used to get bounding box on first frame)")
    ap.add_argument("-r", "--result", required=False, help="Path to the new file when results will be stored")
    ap.add_argument("-border", "--border", action='store_true', help="Flag for running improvement of object crossing left/right border in equirectangular frames")
    ap.add_argument("-nfov", "--nfov", action='store_true', help="Flag for running improvement to track in rectilinear frames (normal field of view)")
    args = vars(ap.parse_args())

    # create instance for evaluation
    if args["border"]:
        border = OpenCVTrackingBorder(args["tracker"], args["video"], args["groundtruth"], args["result"])
        border.startTrackingBorder()
    elif args["nfov"]:
        nfov = OpenCVTrackingNFOV(args["tracker"], args["video"], args["groundtruth"], args["result"])
        nfov.startTrackingNFOV()
    else:
        default = OpenCVTrackingDefault(args["tracker"], args["video"], args["groundtruth"], args["result"])
        default.startTrackingDefault()
