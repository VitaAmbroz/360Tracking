#################################################################################################
# Visual object tracking in panoramic video
# Master thesis at Brno University of Technology - Faculty of Information Technology
# Author:       Vít Ambrož (xambro15@stud.fit.vutbr.cz)
# Supervisor:   Doc. Ing. Martin Čadík, Ph.D.
# Module:       run_video_360.py
# Description:  Top level module for running equirectangular improvements of SiamDW and Ocean Trackers
#################################################################################################

import os
import sys
import argparse

from ocean_360_default import Ocean360Default
from ocean_360_border import Ocean360Border
from ocean_360_nfov import Ocean360NFOV
from siamdw_360_default import SiamDW360Default
from siamdw_360_border import SiamDW360Border
from siamdw_360_nfov import SiamDW360NFOV


def main():
    parser = argparse.ArgumentParser(description='Run the tracker on 360 video.')
    parser.add_argument("-arch", "--arch", type=str, required=True, help='Tracker - "Ocean" or "SiamDW"')
    parser.add_argument("-resume", "--resume", type=str, required=True, help='Pretrained model path.')
    parser.add_argument("-v", "--video", type=str, required=True, help='Path to the video file.')
    parser.add_argument("-gt", "--groundtruth", type=str, required=False, help="Path to the file with groundtruth data (Used to get bounding box on first frame)")
    parser.add_argument("-r", "--result", type=str, required=False, help="Path to the new file when results will be stored")
    parser.add_argument("-border", "--border", action='store_true', help="Flag for running improvement of object crossing left/right border in equirectangular frames")
    parser.add_argument("-nfov", "--nfov", action='store_true', help="Flag for running improvement to track in rectilinear frames (normal field of view)")

    args = parser.parse_args()

    # else: 
    if args.arch == "Ocean":
        if args.border:
            ocean = Ocean360Border(args.resume, args.video, args.groundtruth, args.result)
            ocean.run_ocean_border()
        elif args.nfov:
            ocean = Ocean360NFOV(args.resume, args.video, args.groundtruth, args.result)
            ocean.run_ocean_nfov()
        else:
            ocean = Ocean360Default(args.resume, args.video, args.groundtruth, args.result)
            ocean.run_ocean_default()
    elif args.arch == "SiamDW":
        if args.border:
            siamdw = SiamDW360Border(args.resume, args.video, args.groundtruth, args.result)
            siamdw.run_siamdw_border()
        elif args.nfov:
            siamdw = SiamDW360NFOV(args.resume, args.video, args.groundtruth, args.result)
            siamdw.run_siamdw_nfov()
        else:
            siamdw = SiamDW360Default(args.resume, args.video, args.groundtruth, args.result)
            siamdw.run_siamdw_default()
    else:
        print("Invalid --arch parameter - possible Ocean or SiamDW")
        sys.exit(-1)
        

if __name__ == '__main__':
    main()
