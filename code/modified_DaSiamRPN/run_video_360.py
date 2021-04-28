#################################################################################################
# Visual object tracking in panoramic video
# Master thesis at Brno University of Technology - Faculty of Information Technology
# Author:       Vít Ambrož (xambro15@stud.fit.vutbr.cz)
# Supervisor:   Doc. Ing. Martin Čadík, Ph.D.
# Module:       run_video_360.py
# Description:  Top level module for running equirectangular improvements of DaSiamRPN tracker
#################################################################################################

import os
import sys
import argparse

from tracker_360_default import Tracker360Default
from tracker_360_border import Tracker360Border
from tracker_360_nfov import Tracker360NFOV


def main():
    parser = argparse.ArgumentParser(description='Run the tracker on 360 video.')
    parser.add_argument("-v", "--video", type=str, required=True, help='Path to the video file.')
    parser.add_argument("-gt", "--groundtruth", type=str, required=False, help="Path to the file with groundtruth data (Used to get bounding box on first frame)")
    parser.add_argument("-r", "--result", type=str, required=False, help="Path to the new file when results will be stored")
    parser.add_argument("-border", "--border", action='store_true', help="Flag for running improvement of object crossing left/right border in equirectangular frames")
    parser.add_argument("-nfov", "--nfov", action='store_true', help="Flag for running improvement to track in rectilinear frames (normal field of view)")

    args = parser.parse_args()

    if args.border:
        tracker = Tracker360Border(args.video, args.groundtruth, args.result)
        tracker.run_video_border()
    elif args.nfov:
        tracker = Tracker360NFOV(args.video, args.groundtruth, args.result)
        tracker.run_video_nfov()
    else:    
        tracker = Tracker360Default(args.video, args.groundtruth, args.result)
        tracker.run_video_default()
        

if __name__ == '__main__':
    main()
