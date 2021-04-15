#################################################################################################
# Visual object tracking in panoramic video
# Master thesis at Brno University of Technology - Faculty of Information Technology
# Author:       Vít Ambrož (xambro15@stud.fit.vutbr.cz)
# Supervisor:   Doc. Ing. Martin Čadík, Ph.D.
# Module:       run_evaluation_tool.py
# Description:  Top level of evaluation single object trackers in custom groundtruth dataset
#################################################################################################

import argparse
import os
import sys

from annotation.evaluation import Evaluation

###############################################################
###############            MAIN              ##################
###############################################################
if __name__ == '__main__':
    # construct the argument parser and parse the arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-gt", "--groundtruth", required=False, help="Path to the file with groundtruth data")
    ap.add_argument("-result", "--result", required=False, help="Path to the file with tracking result data")
    ap.add_argument("-video", "--video", required=False, help="Path to the video")
    ap.add_argument("-img", "--img", required=False, help="Path to images sequence")
    ap.add_argument("-demo", "--demo", action='store_true', help="Path to the dataset-demo directory - annotation/dataset-demo/demo-annotation/.")
    args = vars(ap.parse_args())

    # handle video/img/demo path
    # get path to the video
    path = args["video"]
    # get path of images seq
    if not(path) and args["img"]:
        path = args["img"]
    # get path of demo
    if not(path) and args["demo"]:
        path = "annotation/dataset-demo/demo-annotation/demo.mp4"
    # no path given !
    if not(path):
        print("Video file path missing -> run_evaluation.py -help")
        sys.exit(-1)

    # handle groundtruth path
    gt_path = args["groundtruth"]
    # get demo groundtruth
    if not(gt_path) and args["demo"]:
        gt_path = "annotation/dataset-demo/demo-annotation/groundtruth.txt"
    # no path given !
    if not(gt_path):
        print("Groundtruth data file path missing -> run_evaluation.py -help")
        sys.exit(-1)

    # handle result path
    result_path = args["result"]
    # get demo groundtruth
    if not(result_path) and args["demo"]:
        result_path = "annotation/dataset-demo/demo-result/demo-result-CSRT.txt"
    # no path given !
    if not(result_path):
        print("Result data file path missing -> run_evaluation.py -help")
        sys.exit(-1)


    # create instance for evaluation
    evaluation = Evaluation(path, gt_path, result_path)

    if args["img"]:
        # run drawing on images sequence
        evaluation.runImageSeq()
    else:
        # run video (that is default, flag -v is there just for strict call)
        evaluation.runVideo()
