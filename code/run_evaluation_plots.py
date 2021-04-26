#################################################################################################
# Visual object tracking in panoramic video
# Master thesis at Brno University of Technology - Faculty of Information Technology
# Author:       Vít Ambrož (xambro15@stud.fit.vutbr.cz)
# Supervisor:   Doc. Ing. Martin Čadík, Ph.D.
# Module:       run_evaluation_plots.py
# Description:  TODO
#################################################################################################

import argparse
import os
import sys

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from code.annotation import EvaluationPlots

###############################################################
###############            MAIN              ##################
###############################################################
if __name__ == '__main__':
    # construct the argument parser and parse the arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-t", "--tracker", required=False, help="Tracker results folder name, e.g. CSRT")
    ap.add_argument("-n", "--number", required=False, help="Number of videosequence in custom dataset, possible 01-21")
    args = vars(ap.parse_args())


    # create instance for drawing evaluation plot
    evaluation = EvaluationPlots(tracker = args["tracker"], seq_number = args["number"])
    evaluation.createPlot()
