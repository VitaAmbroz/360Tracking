#################################################################################################
# Visual object tracking in panoramic video
# Master thesis at Brno University of Technology - Faculty of Information Technology
# Author:       Vít Ambrož (xambro15@stud.fit.vutbr.cz)
# Supervisor:   Doc. Ing. Martin Čadík, Ph.D.
# Module:       run_anova.py
# Description:  Top level for experiments with ANOVA (Analysis of Variance)
#################################################################################################

import os
import sys

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from code.annotation import Anova

if __name__ == '__main__':
    anova = Anova()
    anova.run3WayAnovaAUC()
    # anova.run3WayAnovaCenterError()
    # anova.run2WayAnovaAUC()
    # anova.run2WayAnovaCenterError()