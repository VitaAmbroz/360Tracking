#################################################################################################
# Visual object tracking in panoramic video
# Master thesis at Brno University of Technology - Faculty of Information Technology
# Author:       Vít Ambrož (xambro15@stud.fit.vutbr.cz)
# Supervisor:   Doc. Ing. Martin Čadík, Ph.D.
# Module:       run_video_360.py
# Description:  Top level module for running equirectangular improvements of ECO, ATOM, DiMP and KYS trackers
#################################################################################################

import os
import sys
import argparse

env_path = os.path.join(os.path.dirname(__file__), '..')
if env_path not in sys.path:
    sys.path.append(env_path)

from pytracking.evaluation import Tracker360Default
from pytracking.evaluation import Tracker360Border
from pytracking.evaluation import Tracker360NFOV


def main():
    parser = argparse.ArgumentParser(description='Run the tracker on your webcam.')
    parser.add_argument('tracker_name', type=str, help='Name of tracking method.')
    parser.add_argument('tracker_param', type=str, help='Name of parameter file.')
    parser.add_argument('videofile', type=str, help='path to a video file.')
    parser.add_argument("-gt", "--groundtruth", type=str, required=False, help="Path to the file with groundtruth data (Used to get bounding box on first frame)")
    parser.add_argument("-r", "--result", type=str, required=False, help="Path to the new file when results will be stored")
    parser.add_argument("-border", "--border", action='store_true', help="Flag for running improvement of object crossing left/right border in equirectangular frames")
    parser.add_argument("-nfov", "--nfov", action='store_true', help="Flag for running improvement to track in rectilinear frames (normal field of view)")

    args = parser.parse_args()

    if args.border:
        tracker = Tracker360Border(args.tracker_name, args.tracker_param, args.videofile, args.groundtruth, args.result)
        tracker.run_video_border()
    elif args.nfov:
        tracker = Tracker360NFOV(args.tracker_name, args.tracker_param, args.videofile, args.groundtruth, args.result)
        tracker.run_video_nfov()
    else:    
        tracker = Tracker360Default(args.tracker_name, args.tracker_param, args.videofile, args.groundtruth, args.result)
        tracker.run_video_default()
        

if __name__ == '__main__':
    main()
