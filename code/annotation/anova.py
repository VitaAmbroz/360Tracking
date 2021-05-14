
#################################################################################################
# Visual object tracking in panoramic video
# Master thesis at Brno University of Technology - Faculty of Information Technology
# Author:       Vít Ambrož (xambro15@stud.fit.vutbr.cz)
# Supervisor:   Doc. Ing. Martin Čadík, Ph.D.
# Module:       anova.py
# Description:  Experiments with results and 3-WAY and 2-WAY ANOVA (Analysis of Variance)
# Sources:      - https://www.pythonfordatascience.org/factorial-anova-python/
#               - https://www.statsmodels.org/dev/anova.html#module-statsmodels.stats.anova
#################################################################################################

import numpy as np
import torch

import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols

import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns


class Anova:
    """Computing 3-way and 2-way ANOVA for AUC and Precision metrics"""
    def __init__(self):
        # paths for IoU files
        self.PATH_IOU_DEFAULT = "annotation/results/<TRACKER>/<NUMBER>/<NUMBER>-result-default-iou.txt"
        self.PATH_IOU_BORDER = "annotation/results/<TRACKER>/<NUMBER>/<NUMBER>-result-border-iou.txt"
        self.PATH_IOU_NFOV = "annotation/results/<TRACKER>/<NUMBER>/<NUMBER>-result-nfov-iou.txt"
        
        # paths for center error files
        self.PATH_CENTER_ERROR_DEFAULT = "annotation/results/<TRACKER>/<NUMBER>/<NUMBER>-result-default-centererror.txt"
        self.PATH_CENTER_ERROR_BORDER = "annotation/results/<TRACKER>/<NUMBER>/<NUMBER>-result-border-centererror.txt"
        self.PATH_CENTER_ERROR_NFOV = "annotation/results/<TRACKER>/<NUMBER>/<NUMBER>-result-nfov-centererror.txt"

        # constants of improvements
        self.IMPROVEMENTS = ["DEFAULT", "BORDER", "NFOV"]
        # constants of trackers names
        self.TRACKERS = ["MIL","MEDIANFLOW","TLD","KCF","CSRT","ECO","ATOM","DaSiamRPN","SiamDW","DiMP","KYS","Ocean"]
        # constant of whole dataset with total 21 sequences
        self.DATASET = ["01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21"]

        # constant of whole dataset with total 13 sequences where object crosses equirectangular border
        self.DATASET_CROSSING_BORDER = ["01","02","03","04","08","11","12","13","14","15","16","18","21"]
        # constant of whole dataset with total 8 sequences where object does not crosses equirectangular border
        self.DATASET_NOT_CROSSING_BORDER = ["05","06","07","09","10","17","19","20"]
    

    def _parseGivenDataFile(self, path):
        """Method for parsing float numbers from given file"""
        dataFile = open(path, 'r')
        lines = dataFile.readlines()

        # init empty list
        floatList = []
        # parse lines containing float value of intersection over union
        for line in lines:
            f = float(line)
            floatList.append(f)

        return floatList



    ##################################################################################################
    ##################################### 3-Way ANOVA for AUC metric #################################
    ##################################################################################################
    def _getAUCAllTrackersSequence(self, seq_number: str, default=False, border=False, nfov=False):
        """Returns AUC values of all trackers for given sequence as tensor"""
        plot_bin_gap = 0.05
        threshold_set_overlap = torch.arange(0.0, 1.0 + plot_bin_gap, plot_bin_gap, dtype=torch.float64)
        ave_success_rate_plot_overlap = torch.zeros((len(self.TRACKERS), threshold_set_overlap.numel()), dtype=torch.float32)

        path = ""
        if default:
            path = self.PATH_IOU_DEFAULT
        elif border:
            path = self.PATH_IOU_BORDER
        elif nfov:
            path = self.PATH_IOU_NFOV

        for i in range(len(self.TRACKERS)):
            # load and parse data
            current_path = path.replace("<TRACKER>", self.TRACKERS[i]).replace("<NUMBER>", seq_number)
            iou = self._parseGivenDataFile(current_path)

            # transform python lists to tensors
            iou_tensor = torch.Tensor(iou)

            # success computing
            ave_success_rate_plot_overlap[i,:] = (iou_tensor.view(-1, 1) > threshold_set_overlap.view(1, -1)).sum(0).float() / len(iou)

        # auc_curve as mean of ave_success_rate_plot_overlap tensors
        auc_curve = ave_success_rate_plot_overlap * 100.0

        auc = []
        for i in range(len(self.TRACKERS)):
            # compute AUC (area under curve for 12 results/IoU)
            auc_next = auc_curve[i].mean(-1).item()
            # concatenate to tensor list
            auc.append(auc_next)
        # python list to tensor
        auc = torch.Tensor(auc)

        return auc


    def run3WayAnovaAUC(self):
        """Computes 3-way ANOVA for AUC and factors - sequence, improvement, tracker"""
        g1 = []
        g2 = []
        g3 = []
        TRACKERS_SHORTCUTS = ["MIL","MFLOW","TLD","KCF","CSRT","ECO","ATOM","DSRPN","SiamDW","DiMP","KYS","Ocean"]

        for i in range(len(self.DATASET_NOT_CROSSING_BORDER)):
            for j in range(len(self.IMPROVEMENTS)):
                for k in range(len(TRACKERS_SHORTCUTS)):
                    g1.append(self.DATASET_NOT_CROSSING_BORDER[i])
                    g2.append(self.IMPROVEMENTS[j])
                    g3.append(TRACKERS_SHORTCUTS[k])

        auc = []
        for i in range(len(self.DATASET_NOT_CROSSING_BORDER)):
            default_auc_i = self._getAUCAllTrackersSequence(seq_number=self.DATASET_NOT_CROSSING_BORDER[i], default=True).tolist()
            border_auc_i = self._getAUCAllTrackersSequence(seq_number=self.DATASET_NOT_CROSSING_BORDER[i], border=True).tolist()
            nfov_auc_i = self._getAUCAllTrackersSequence(seq_number=self.DATASET_NOT_CROSSING_BORDER[i], nfov=True).tolist()
            # concat
            auc = auc + default_auc_i + border_auc_i + nfov_auc_i
        
        auc_rounded = [round(num / 100, 3) for num in auc]
        # print(auc_rounded)

        df = pd.DataFrame(list(zip(auc_rounded, g1, g2, g3)), columns=['AUC', 'sequence', 'improvement', 'tracker'], dtype=np.float64)
        print(df)
        
        # 3Way anova - https://www.pythonfordatascience.org/factorial-anova-python/
        model = ols("AUC ~ C(sequence, Sum) + C(improvement, Sum) + C(tracker, Sum) + C(sequence, Sum):C(improvement, Sum) + C(sequence, Sum):C(tracker, Sum) + C(improvement, Sum):C(tracker, Sum)", data=df).fit()
        # model = ols("auc ~ C(sequence) + C(improvement) + C(tracker) + C(sequence):C(improvement) + C(sequence):C(tracker) + C(improvement):C(tracker)", data=df).fit()
        aov_table = sm.stats.anova_lm(model, typ=3)
        print(aov_table)
    

        # generating boxplot
        matplotlib.rcParams.update({'font.size': 18})
        matplotlib.rcParams.update({'axes.labelsize': 18})
        
        # inspired and modified from https://www.reneshbedre.com/blog/anova.html
        # set custom color palette    
        colors = ["#ff6666", "#66ff66", "#0080ff"]
        sns.set_palette(sns.color_palette(colors))
        # create boxplot
        ax = sns.boxplot(x='tracker', y='AUC', data=df, linewidth=2, hue="improvement")
        # ax = sns.catplot(x="improvement", y="auc", kind="swarm", data=df)
        plt.show()

    

    ##################################################################################################
    ############################### 3-Way ANOVA for Distance Error metric ############################
    ##################################################################################################
    def _getCerrorAllTrackersSequence(self, seq_number: str, default=False, border=False, nfov=False):
        """Returns Precision values of all trackers for given sequence as tensor"""
        threshold_set_center = torch.arange(0, 51, dtype=torch.float64)
        ave_success_rate_plot_center = torch.zeros((len(self.TRACKERS), threshold_set_center.numel()), dtype=torch.float32)

        path = ""
        if default:
            path = self.PATH_CENTER_ERROR_DEFAULT
        elif border:
            path = self.PATH_CENTER_ERROR_BORDER
        elif nfov:
            path = self.PATH_CENTER_ERROR_NFOV

        for i in range(len(self.TRACKERS)):
            # load and parse data
            current_path = path.replace("<TRACKER>", self.TRACKERS[i]).replace("<NUMBER>", seq_number)
            cerror = self._parseGivenDataFile(current_path)

            # transform python lists to tensors
            cerror_tensor = torch.Tensor(cerror)

            # success computing
            ave_success_rate_plot_center[i,:] = (cerror_tensor.view(-1, 1) <= threshold_set_center.view(1, -1)).sum(0).float() / len(cerror)

        # create curves
        prec_curve = ave_success_rate_plot_center * 100.0
        # score should be counted for max 20 pixel error
        prec_score = prec_curve[:, 20]

        return prec_score


    def run3WayAnovaCenterError(self):
        """Computes 3-way ANOVA for Precision and factors - sequence, improvement, tracker"""
        g1 = []
        g2 = []
        g3 = []
        TRACKERS_SHORTCUTS = ["MIL","MFLOW","TLD","KCF","CSRT","ECO","ATOM","DSRPN","SiamDW","DiMP","KYS","Ocean"]

        for i in range(len(self.DATASET)):
            for j in range(len(self.IMPROVEMENTS)):
                for k in range(len(TRACKERS_SHORTCUTS)):
                    g1.append(self.DATASET[i])
                    g2.append(self.IMPROVEMENTS[j])
                    g3.append(TRACKERS_SHORTCUTS[k])

        cerror = []
        for i in range(len(self.DATASET)):
            default_cerror_i = self._getCerrorAllTrackersSequence(seq_number=self.DATASET[i], default=True).tolist()
            border_cerror_i = self._getCerrorAllTrackersSequence(seq_number=self.DATASET[i], border=True).tolist()
            nfov_cerror_i = self._getCerrorAllTrackersSequence(seq_number=self.DATASET[i], nfov=True).tolist()
            # concat
            cerror = cerror + default_cerror_i + border_cerror_i + nfov_cerror_i
        
        cerror_rounded = [round(num / 100, 3) for num in cerror]
        # print(cerror_rounded)

        df = pd.DataFrame(list(zip(cerror_rounded, g1, g2, g3)), columns=['LocationError', 'sequence', 'improvement', 'tracker'], dtype=np.float64)
        print(df)
        
        # 3Way anova - https://www.pythonfordatascience.org/factorial-anova-python/
        model = ols("LocationError ~ C(sequence, Sum) + C(improvement, Sum) + C(tracker, Sum) + C(sequence, Sum):C(improvement, Sum) + C(sequence, Sum):C(tracker, Sum) + C(improvement, Sum):C(tracker, Sum)", data=df).fit()
        # model = ols("LocationError ~ C(sequence) + C(improvement) + C(tracker) + C(sequence):C(improvement) + C(sequence):C(tracker) + C(improvement):C(tracker)", data=df).fit()
        aov_table = sm.stats.anova_lm(model, typ=3)
        print(aov_table)


        matplotlib.rcParams.update({'font.size': 18})
        matplotlib.rcParams.update({'axes.labelsize': 18})
        
        # inspired and modified from https://www.reneshbedre.com/blog/anova.html
        # set custom color palette    
        colors = ["#ff6666", "#66ff66", "#0080ff"]
        sns.set_palette(sns.color_palette(colors))
        # create boxplot
        ax = sns.boxplot(x='tracker', y='LocationError', data=df, linewidth=2, hue="improvement")
        # ax = sns.catplot(x="tracker", y="auc", kind="swarm", data=df)
        plt.show()



    ##################################################################################################
    ##################################### 2-Way ANOVA for AUC metric #################################
    ##################################################################################################
    def _getAUCAllTrackers(self, default=False, border=False, nfov=False):
        """Returns AUC values of all trackers for all sequences as tensor"""
        dataset = self.DATASET

        plot_bin_gap = 0.05
        threshold_set_overlap = torch.arange(0.0, 1.0 + plot_bin_gap, plot_bin_gap, dtype=torch.float64)
        ave_success_rate_plot_overlap = torch.zeros((len(dataset), len(self.TRACKERS), threshold_set_overlap.numel()), dtype=torch.float32)

        if default:
            path = self.PATH_IOU_DEFAULT
        elif border:
            path = self.PATH_IOU_BORDER
        elif nfov:
            path = self.PATH_IOU_NFOV

        for i in range(len(dataset)):
            for j in range(len(self.TRACKERS)):
                # load and parse data
                current_path = path.replace("<TRACKER>", self.TRACKERS[j]).replace("<NUMBER>", dataset[i])
                iou = self._parseGivenDataFile(current_path)

                # transform python lists to tensors
                iou_tensor = torch.Tensor(iou)

                # success computing
                ave_success_rate_plot_overlap[i,j,:] = (iou_tensor.view(-1, 1) > threshold_set_overlap.view(1, -1)).sum(0).float() / len(iou)

        # auc_curve as mean of ave_success_rate_plot_overlap tensors
        auc_curve = ave_success_rate_plot_overlap.mean(0) * 100.0
        auc = auc_curve.mean(-1)

        return auc


    def run2WayAnovaAUC(self):
        """Computes 2-way ANOVA for AUC and factors - improvement, tracker"""
        g1 = []
        g2 = []
        for i in range(len(self.IMPROVEMENTS)):
            for j in range(len(self.TRACKERS)):
                g1.append(self.IMPROVEMENTS[i])
                g2.append(self.TRACKERS[j])

        default_auc = self._getAUCAllTrackers(default=True).tolist()
        border_auc = self._getAUCAllTrackers(border=True).tolist()
        nfov_auc = self._getAUCAllTrackers(nfov=True).tolist()
        # concat
        auc = default_auc + border_auc + nfov_auc
        auc_rounded = [round(num / 100, 3) for num in auc]

        df = pd.DataFrame(list(zip(auc_rounded, g1, g2)), columns=['auc', 'improvement', 'tracker'], dtype=np.float64)
        print(df)

        # Type 2 ANOVA DataFrame - https://www.statsmodels.org/dev/anova.html#module-statsmodels.stats.anova
        df_lm = ols('auc ~ C(improvement, Sum) + C(tracker, Sum)', data=df).fit()
        # df_lm = ols('auc ~ C(improvement) + C(tracker)', data=df).fit()
        table = sm.stats.anova_lm(df_lm, typ=2) 
        print(table)
    

    ##################################################################################################
    ############################### 2-Way ANOVA for Distance Error metric ############################
    ##################################################################################################
    def _getCerrorAllTrackers(self, default=False, border=False, nfov=False):
        """Returns Precision values of all trackers for all sequences as tensor"""
        dataset = self.DATASET
        
        threshold_set_center = torch.arange(0, 51, dtype=torch.float64)
        ave_success_rate_plot_center = torch.zeros((len(dataset), len(self.TRACKERS), threshold_set_center.numel()), dtype=torch.float32)

        path = ""
        if default:
            path = self.PATH_CENTER_ERROR_DEFAULT
        elif border:
            path = self.PATH_CENTER_ERROR_BORDER
        elif nfov:
            path = self.PATH_CENTER_ERROR_NFOV

        for i in range(len(dataset)):
            for j in range(len(self.TRACKERS)):
                # load and parse data
                current_path = path.replace("<TRACKER>", self.TRACKERS[j]).replace("<NUMBER>", dataset[i])
                cerror = self._parseGivenDataFile(current_path)

                # transform python lists to tensors
                cerror_tensor = torch.Tensor(cerror)

                # success computing
                ave_success_rate_plot_center[i,j,:] = (cerror_tensor.view(-1, 1) <= threshold_set_center.view(1, -1)).sum(0).float() / len(cerror)

        # create curves
        prec_curve = ave_success_rate_plot_center.mean(0) * 100.0
        # score should be counted for max 20 pixel error
        prec_score = prec_curve[:, 20]

        return prec_score


    def run2WayAnovaCenterError(self):
        """Computes 2-way ANOVA for Precision and factors - improvement, tracker"""
        g1 = []
        g2 = []
        for i in range(len(self.IMPROVEMENTS)):
            for j in range(len(self.TRACKERS)):
                g1.append(self.IMPROVEMENTS[i])
                g2.append(self.TRACKERS[j])

        default_cerror = self._getCerrorAllTrackers(default=True).tolist()
        border_cerror = self._getCerrorAllTrackers(border=True).tolist()
        nfov_cerror = self._getCerrorAllTrackers(nfov=True).tolist()
        # concat
        cerror = default_cerror + border_cerror + nfov_cerror
        cerror_rounded = [round(num / 100, 3) for num in cerror]

        df = pd.DataFrame(list(zip(cerror_rounded, g1, g2)), columns=['cerror', 'improvement', 'tracker'], dtype=np.float64)
        print(df)

        # Type 2 ANOVA DataFrame - https://www.statsmodels.org/dev/anova.html#module-statsmodels.stats.anova
        df_lm = ols('cerror ~ C(improvement, Sum) + C(tracker, Sum)', data=df).fit()
        # df_lm = ols('cerror ~ C(improvement) + C(tracker)', data=df).fit()
        table = sm.stats.anova_lm(df_lm, typ=2) 
        print(table)

