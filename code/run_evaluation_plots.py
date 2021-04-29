#################################################################################################
# Visual object tracking in panoramic video
# Master thesis at Brno University of Technology - Faculty of Information Technology
# Author:       Vít Ambrož (xambro15@stud.fit.vutbr.cz)
# Supervisor:   Doc. Ing. Martin Čadík, Ph.D.
# Module:       run_evaluation_plots.py
# Description:  Top module for drawing success, precision, variance plots
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
    ap.add_argument("-success", "--success", action='store_true', help="Draw success plot (based on IoU metric)")
    ap.add_argument("-precision", "--precision", action='store_true', help="Draw precision plot (based on center error metric)")
    ap.add_argument("-allsequences", "--allsequences", action='store_true', help="Flag for drawing plot for average result of all 21 video sequences")
    ap.add_argument("-alltrackers", "--alltrackers", action='store_true', help="Flag for drawing plot with all 12 trackers")
    args = vars(ap.parse_args())

    # create instance for drawing evaluation plot
    evaluation = EvaluationPlots()

    # default success if not specified
    if not(args["success"]) and not(args["precision"]):
        args["success"] = True

    if args["success"]:
        if args["tracker"] and args["number"]:
            evaluation.createSuccessPlot(tracker=args["tracker"], seq_number=args["number"])
        elif args["tracker"] and args["allsequences"]:
            evaluation.createSuccessPlotAllSequences(tracker=args["tracker"])
            # evaluation.createSuccessPlotAllSequencesVariance(tracker=args["tracker"])
        elif args["alltrackers"]:
            evaluation.createSuccessPlotAllTrackers(default=True)
            evaluation.createSuccessPlotAllTrackers(border=True)
            evaluation.createSuccessPlotAllTrackers(nfov=True)
        else:
            print("Invalid combination of arguments, run: 'python run_evaluation_plots --help")
            sys.exit(-1)
    elif args["precision"]:
        print("Yea - precision")
    # TODO treshold
