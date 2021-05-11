
import argparse
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