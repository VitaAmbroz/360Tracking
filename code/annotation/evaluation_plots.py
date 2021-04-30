#################################################################################################
# Visual object tracking in panoramic video
# Master thesis at Brno University of Technology - Faculty of Information Technology
# Author:       Vít Ambrož (xambro15@stud.fit.vutbr.cz)
# Supervisor:   Doc. Ing. Martin Čadík, Ph.D.
# Module:       evaluation_plots.py
# Description:  Drawing success, precision, variance plots
#################################################################################################
# This source code has been inspired by:
# https://github.com/visionml/pytracking/blob/master/pytracking/analysis/plot_results.py
# --------------------------------------------------------
# pytracking (https://github.com/visionml/pytracking)
# Licensed under GPL-3.0 License
# Copyright Martin Danelljan, Goutam Bhat
# --------------------------------------------------------
#################################################################################################

import sys
import glob
import os
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import torch


class EvaluationPlots:
    """Drawing success, precision, variance plots"""
    def __init__(self):
        # paths for IoU files
        self.PATH_IOU_DEFAULT = "annotation/results/<TRACKER>/<NUMBER>/<NUMBER>-result-default-iou.txt"
        self.PATH_IOU_BORDER = "annotation/results/<TRACKER>/<NUMBER>/<NUMBER>-result-border-iou.txt"
        self.PATH_IOU_NFOV = "annotation/results/<TRACKER>/<NUMBER>/<NUMBER>-result-nfov-iou.txt"
        
        # paths for center error files
        self.PATH_CENTER_ERROR_DEFAULT = "annotation/results/<TRACKER>/<NUMBER>/<NUMBER>-result-default-centererror.txt"
        self.PATH_CENTER_ERROR_BORDER = "annotation/results/<TRACKER>/<NUMBER>/<NUMBER>-result-border-centererror.txt"
        self.PATH_CENTER_ERROR_NFOV = "annotation/results/<TRACKER>/<NUMBER>/<NUMBER>-result-nfov-centererror.txt"

        # constants of trackers names and dataset sequences
        self.TRACKERS = ["ECO","ATOM","DiMP","KYS","DaSiamRPN","Ocean","SiamDW","CSRT","MEDIANFLOW","KCF","MIL","TLD"]
        self.DATASET = ["01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21"]

        # paths for result plots in .pdf
        self.PATH_SUCCESS_PLOT = "annotation/results/<TRACKER>/<NUMBER>/<NUMBER>-success-plot"
        self.PATH_SUCCESS_PLOT_ALLSEQUENCES = "annotation/results/total-success/<TRACKER>-success-plot"
        self.PATH_SUCCESS_PLOT_ALLSEQUENCES_VAR = "annotation/results/total-success/<TRACKER>-success-plot-variance"
        self.PATH_SUCCESS_PLOT_ALLTRACKERS = "annotation/results/total-success/all-trackers-success-plot"
        self.PATH_SUCCESS_PLOT_ALLTRACKERS_SEQ = "annotation/results/total-success/all-trackers/<NUMBER>-trackers-success-plot"

        self.PATH_PRECISION_PLOT = "annotation/results/<TRACKER>/<NUMBER>/<NUMBER>-precision-plot"
        self.PATH_PRECISION_PLOT_ALLSEQUENCES = "annotation/results/total-precision/<TRACKER>-precision-plot"
        self.PATH_PRECISION_PLOT_ALLTRACKERS = "annotation/results/total-precision/all-trackers-precision-plot"
        self.PATH_PRECISION_PLOT_ALLTRACKERS_SEQ = "annotation/results/total-precision/all-trackers/<NUMBER>-trackers-precision-plot"

    
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


    def _getPlotDrawStyles(self):
        """Gets colors and line styles for drawed plot lines"""
        plot_draw_style = [{'color': (1.0, 0.0, 0.0), 'line_style': '-'},
                        {'color': (0.0, 1.0, 0.0), 'line_style': '-'},
                        {'color': (0.0, 0.0, 1.0), 'line_style': '-'},
                        {'color': (0.0, 0.0, 0.0), 'line_style': '-'},
                        {'color': (1.0, 0.0, 1.0), 'line_style': '-'},
                        {'color': (0.0, 1.0, 1.0), 'line_style': '-'},
                        {'color': (0.5, 0.5, 0.5), 'line_style': '-'},
                        {'color': (136.0 / 255.0, 0.0, 21.0 / 255.0), 'line_style': '--'},
                        {'color': (1.0, 127.0 / 255.0, 39.0 / 255.0), 'line_style': '--'},
                        {'color': (0.0, 162.0 / 255.0, 232.0 / 255.0), 'line_style': '--'},
                        {'color': (0.0, 0.5, 0.0), 'line_style': '--'},
                        {'color': (0.2, 0.1, 0.7), 'line_style': '--'},
                        {'color': (0.4, 0.7, 0.1), 'line_style': '--'},
                        {'color': (0.1, 0.4, 0.0), 'line_style': '--'},
                        {'color': (1.0, 0.5, 0.2), 'line_style': '--'},
                        {'color': (0.6, 0.3, 0.9), 'line_style': '--'},
                        {'color': (0.7, 0.6, 0.2), 'line_style': '--'}]

        return plot_draw_style


    def _plotDrawSave(self, y, x, scores, trackers, plot_draw_styles, plot_opts, save_path):
        """Draws and save given success or precision plot settings"""
        # Plot settings
        font_size = plot_opts.get('font_size', 12)
        font_size_axis = plot_opts.get('font_size_axis', 12)
        line_width = plot_opts.get('line_width', 2)
        font_size_legend = plot_opts.get('font_size_legend', 12)
        bbox_to_anchor = plot_opts.get('bbox_to_anchor', None)
        ncol = plot_opts.get('ncol', 1)

        plot_type = plot_opts['plot_type']
        legend_loc = plot_opts['legend_loc']

        xlabel = plot_opts['xlabel']
        ylabel = plot_opts['ylabel']
        xlim = plot_opts['xlim']
        ylim = plot_opts['ylim']

        title = plot_opts['title']

        matplotlib.rcParams.update({'font.size': font_size})
        matplotlib.rcParams.update({'axes.titlesize': font_size_axis})
        matplotlib.rcParams.update({'axes.titleweight': 'black'})
        matplotlib.rcParams.update({'axes.labelsize': font_size_axis})

        fig, ax = plt.subplots()

        # possible sort according to best auc
        index_sort = scores.argsort(descending=False)
        # index_sort = torch.Tensor([0,1,2])

        plotted_lines = []
        legend_text = []

        for id, id_sort in enumerate(index_sort):
            # line = ax.plot(x.tolist(), y[id_sort, :].tolist(), linewidth=line_width, color=plot_draw_styles[index_sort.numel() - id - 1]['color'], linestyle=plot_draw_styles[index_sort.numel() - id - 1]['line_style'])
            line = ax.plot(x.tolist(), y[id_sort, :].tolist(), linewidth=line_width, color=plot_draw_styles[id_sort.item()]['color'], linestyle=plot_draw_styles[id_sort.item()]['line_style'])

            plotted_lines.append(line[0])

            tracker = trackers[id_sort]
            disp_name = tracker

            legend_text.append('{} [{:.1f}]'.format(disp_name, scores[id_sort]))


        ax.legend(plotted_lines[::-1], legend_text[::-1], loc=legend_loc, bbox_to_anchor=bbox_to_anchor, ncol=ncol, fancybox=False, edgecolor='black', fontsize=font_size_legend, framealpha=1.0)

        ax.set(xlabel=xlabel, ylabel=ylabel, xlim=xlim, ylim=ylim, title=title)

        ax.grid(True, linestyle='-.')
        fig.tight_layout()

        # tikzplotlib.save('{}/{}_plot.tex'.format(result_plot_path, plot_type))
        pdf_path = save_path + ".pdf"
        fig.savefig(pdf_path, dpi=300, format='pdf', transparent=True)
        plt.draw()
        print("File " + pdf_path + " has been created.")
        # plt.show()


    ################################################################################
    ############################### Success plots ##################################
    ################################################################################
    def createSuccessPlot(self, tracker: str, seq_number: str):
        """Draws and saves success plot for given tracker and sequence"""
        self.PATH_IOU_DEFAULT = self.PATH_IOU_DEFAULT.replace("<TRACKER>", tracker).replace("<NUMBER>", seq_number)
        self.PATH_IOU_BORDER = self.PATH_IOU_BORDER.replace("<TRACKER>", tracker).replace("<NUMBER>", seq_number)
        self.PATH_IOU_NFOV = self.PATH_IOU_NFOV.replace("<TRACKER>", tracker).replace("<NUMBER>", seq_number)

        iou_default = self._parseGivenDataFile(self.PATH_IOU_DEFAULT)
        iou_border = self._parseGivenDataFile(self.PATH_IOU_BORDER)
        iou_nfov = self._parseGivenDataFile(self.PATH_IOU_NFOV)

        if len(iou_default) > 0 and len(iou_border) > 0 and len(iou_nfov) > 0:
            plot_bin_gap = 0.05
            threshold_set_overlap = torch.arange(0.0, 1.0 + plot_bin_gap, plot_bin_gap, dtype=torch.float64)
            ave_success_rate_plot_overlap = torch.zeros((3, threshold_set_overlap.numel()), dtype=torch.float32)
            
            # transform python list to tensors
            iou_default_tensor = torch.Tensor(iou_default)
            iou_border_tensor = torch.Tensor(iou_border)
            iou_nfov_tensor = torch.Tensor(iou_nfov)

            # success computing
            ave_success_rate_plot_overlap[0] = (iou_default_tensor.view(-1, 1) > threshold_set_overlap.view(1, -1)).sum(0).float() / len(iou_default)
            ave_success_rate_plot_overlap[1] = (iou_border_tensor.view(-1, 1) > threshold_set_overlap.view(1, -1)).sum(0).float() / len(iou_border)
            ave_success_rate_plot_overlap[2] = (iou_nfov_tensor.view(-1, 1) > threshold_set_overlap.view(1, -1)).sum(0).float() / len(iou_nfov)

            auc_curve = ave_success_rate_plot_overlap * 100.0

            # compute AUC (area under curve for 3 results/IoU)
            auc1 = auc_curve[0].mean(-1)
            auc2 = auc_curve[1].mean(-1)
            auc3 = auc_curve[2].mean(-1)
            # concatenate to tensor list
            auc = torch.Tensor([auc1, auc2, auc3])

            print(auc_curve)
            print(auc)

            success_plot_opts = {
                'plot_type': 'success', 
                'legend_loc': 'lower left', 
                'xlabel': 'Overlap threshold',
                'ylabel': 'Overlap Precision [%]', 
                'xlim': (0, 1.0), 'ylim': (0, 100), 
                'title': 'Success plot - ' + tracker,
                'font_size_legend': 11
            }
            
            # tracker(modified) names of lines in plot
            tracker_names = [tracker + "-DEFAULT", tracker + "-BORDER", tracker + "-NFOV"]
            
            self.PATH_SUCCESS_PLOT = self.PATH_SUCCESS_PLOT.replace("<TRACKER>", tracker).replace("<NUMBER>", seq_number)
            self._plotDrawSave(auc_curve, threshold_set_overlap, auc, tracker_names, self._getPlotDrawStyles(), success_plot_opts, self.PATH_SUCCESS_PLOT)

    
    def createSuccessPlotAllSequences(self, tracker: str):
        """Draws and saves success plot for given tracker and all 01-21 video sequences in dataset"""
        plot_bin_gap = 0.05
        threshold_set_overlap = torch.arange(0.0, 1.0 + plot_bin_gap, plot_bin_gap, dtype=torch.float64)
        ave_success_rate_plot_overlap = torch.zeros((len(self.DATASET), 3, threshold_set_overlap.numel()), dtype=torch.float32)

        for i in range(len(self.DATASET)):
            # load and parse data
            path_default = self.PATH_IOU_DEFAULT.replace("<TRACKER>", tracker).replace("<NUMBER>", self.DATASET[i])
            path_border = self.PATH_IOU_BORDER.replace("<TRACKER>", tracker).replace("<NUMBER>", self.DATASET[i])
            path_nfov = self.PATH_IOU_NFOV.replace("<TRACKER>", tracker).replace("<NUMBER>", self.DATASET[i])
            
            iou_default = self._parseGivenDataFile(path_default)
            iou_border = self._parseGivenDataFile(path_border)
            iou_nfov = self._parseGivenDataFile(path_nfov)

            # transform python lists to tensors
            iou_default_tensor = torch.Tensor(iou_default)
            iou_border_tensor = torch.Tensor(iou_border)
            iou_nfov_tensor = torch.Tensor(iou_nfov)

            # success computing
            ave_success_rate_plot_overlap[i,0,:] = (iou_default_tensor.view(-1, 1) > threshold_set_overlap.view(1, -1)).sum(0).float() / len(iou_default)
            ave_success_rate_plot_overlap[i,1,:] = (iou_border_tensor.view(-1, 1) > threshold_set_overlap.view(1, -1)).sum(0).float() / len(iou_border)
            ave_success_rate_plot_overlap[i,2,:] = (iou_nfov_tensor.view(-1, 1) > threshold_set_overlap.view(1, -1)).sum(0).float() / len(iou_nfov)

        # auc_curve as mean of ave_success_rate_plot_overlap tensors
        auc_curve = ave_success_rate_plot_overlap.mean(0) * 100.0
        auc = auc_curve.mean(-1)

        success_plot_opts = {
            'plot_type': 'success', 
            'legend_loc': 'upper right', 
            'xlabel': 'Overlap threshold',
            'ylabel': 'Overlap Precision [%]', 
            'xlim': (0, 1.0), 'ylim': (0, 100), 
            'title': 'Success plot - ' + tracker,
            'font_size_legend': 12,
            'bbox_to_anchor': (1.1, 1.0)
        }
        
        # tracker(modified) names of lines in plot
        tracker_names = [tracker + "-DEFAULT", tracker + "-BORDER", tracker + "-NFOV"]
        
        self.PATH_SUCCESS_PLOT_ALLSEQUENCES = self.PATH_SUCCESS_PLOT_ALLSEQUENCES.replace("<TRACKER>", tracker)
        self._plotDrawSave(auc_curve, threshold_set_overlap, auc, tracker_names, self._getPlotDrawStyles(), success_plot_opts, self.PATH_SUCCESS_PLOT_ALLSEQUENCES)

        
    def createSuccessPlotAllTrackersSequence(self, seq_number: str, default=False, border=False, nfov=False):
        """Draws and saves success plot for all trackers (default/border/nfov) and for given video sequence only"""
        plot_bin_gap = 0.05
        threshold_set_overlap = torch.arange(0.0, 1.0 + plot_bin_gap, plot_bin_gap, dtype=torch.float64)
        ave_success_rate_plot_overlap = torch.zeros((len(self.TRACKERS), threshold_set_overlap.numel()), dtype=torch.float32)

        path = ""
        save_path = self.PATH_SUCCESS_PLOT_ALLTRACKERS_SEQ.replace("<NUMBER>", seq_number)
        tracker_names = self.TRACKERS
        title = "Success plot"
        if default:
            path = self.PATH_IOU_DEFAULT
            save_path += "-default"
            title += " - DEFAULT"
        elif border:
            path = self.PATH_IOU_BORDER
            save_path += "-border"
            title += " - BORDER"
        elif nfov:
            path = self.PATH_IOU_NFOV
            save_path += "-nfov"
            title += " - NFOV"

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
        
        success_plot_opts = {
            'plot_type': 'success', 
            'legend_loc': 'upper right', 
            'xlabel': 'Overlap threshold',
            'ylabel': 'Overlap Precision [%]', 
            'xlim': (0, 1.0), 'ylim': (0, 100), 
            'title': title + " (Sequence " + seq_number + ")",
            'font_size_legend': 10,
            'bbox_to_anchor': (1.25, 1.0)
        }
        
        self._plotDrawSave(auc_curve, threshold_set_overlap, auc, tracker_names, self._getPlotDrawStyles(), success_plot_opts, save_path)


    def createSuccessPlotAllTrackers(self, default=False, border=False, nfov=False):
        """Draws and saves success plot for all trackers (default/border/nfov) and all 01-21 video sequences in dataset"""
        plot_bin_gap = 0.05
        threshold_set_overlap = torch.arange(0.0, 1.0 + plot_bin_gap, plot_bin_gap, dtype=torch.float64)
        ave_success_rate_plot_overlap = torch.zeros((len(self.DATASET), len(self.TRACKERS), threshold_set_overlap.numel()), dtype=torch.float32)

        path = ""
        save_path = self.PATH_SUCCESS_PLOT_ALLTRACKERS
        tracker_names = self.TRACKERS
        title = "Success plot"
        if default:
            path = self.PATH_IOU_DEFAULT
            save_path += "-default"
            title += " - DEFAULT"
        elif border:
            path = self.PATH_IOU_BORDER
            save_path += "-border"
            title += " - BORDER"
        elif nfov:
            path = self.PATH_IOU_NFOV
            save_path += "-nfov"
            title += " - NFOV"

        for i in range(len(self.DATASET)):
            for j in range(len(self.TRACKERS)):
                # load and parse data
                current_path = path.replace("<TRACKER>", self.TRACKERS[j]).replace("<NUMBER>", self.DATASET[i])
                iou = self._parseGivenDataFile(current_path)

                # transform python lists to tensors
                iou_tensor = torch.Tensor(iou)

                # success computing
                ave_success_rate_plot_overlap[i,j,:] = (iou_tensor.view(-1, 1) > threshold_set_overlap.view(1, -1)).sum(0).float() / len(iou)

        # auc_curve as mean of ave_success_rate_plot_overlap tensors
        auc_curve = ave_success_rate_plot_overlap.mean(0) * 100.0
        auc = auc_curve.mean(-1)

        success_plot_opts = {
            'plot_type': 'success', 
            'legend_loc': 'upper right', 
            'xlabel': 'Overlap threshold',
            'ylabel': 'Overlap Precision [%]', 
            'xlim': (0, 1.0), 'ylim': (0, 100), 
            'title': title,
            'font_size_legend': 10,
            'bbox_to_anchor': (1.25, 1.0)
        }
        
        self._plotDrawSave(auc_curve, threshold_set_overlap, auc, tracker_names, self._getPlotDrawStyles(), success_plot_opts, save_path)


    def createSuccessPlotAllSequencesVariance(self, tracker: str):
        """Draws and saves success plot for given tracker and all 01-21 video sequences in dataset with variance min and max"""
        plot_bin_gap = 0.05
        threshold_set_overlap = torch.arange(0.0, 1.0 + plot_bin_gap, plot_bin_gap, dtype=torch.float64)
        ave_success_rate_plot_overlap = torch.zeros((len(self.DATASET), 3, threshold_set_overlap.numel()), dtype=torch.float32)

        for i in range(len(self.DATASET)):
            # load and parse data
            path_default = self.PATH_IOU_DEFAULT.replace("<TRACKER>", tracker).replace("<NUMBER>", self.DATASET[i])
            path_border = self.PATH_IOU_BORDER.replace("<TRACKER>", tracker).replace("<NUMBER>", self.DATASET[i])
            path_nfov = self.PATH_IOU_NFOV.replace("<TRACKER>", tracker).replace("<NUMBER>", self.DATASET[i])
            
            iou_default = self._parseGivenDataFile(path_default)
            iou_border = self._parseGivenDataFile(path_border)
            iou_nfov = self._parseGivenDataFile(path_nfov)

            # transform python lists to tensors
            iou_default_tensor = torch.Tensor(iou_default)
            iou_border_tensor = torch.Tensor(iou_border)
            iou_nfov_tensor = torch.Tensor(iou_nfov)

            # success computing
            ave_success_rate_plot_overlap[i,0,:] = (iou_default_tensor.view(-1, 1) > threshold_set_overlap.view(1, -1)).sum(0).float() / len(iou_default)
            ave_success_rate_plot_overlap[i,1,:] = (iou_border_tensor.view(-1, 1) > threshold_set_overlap.view(1, -1)).sum(0).float() / len(iou_border)
            ave_success_rate_plot_overlap[i,2,:] = (iou_nfov_tensor.view(-1, 1) > threshold_set_overlap.view(1, -1)).sum(0).float() / len(iou_nfov)


        # auc_curve as mean of ave_success_rate_plot_overlap tensors
        auc_curve = ave_success_rate_plot_overlap.mean(0) * 100.0
        auc = auc_curve.mean(-1)
        # maximum in tensors
        max_curve = ave_success_rate_plot_overlap.max(0).values * 100.0
        # minimim in tensors
        min_curve = ave_success_rate_plot_overlap.min(0).values * 100.0

        # tracker(modified) names of lines in plot
        tracker_names = [tracker+"-DEFAULT", tracker+"-BORDER", tracker+"-NFOV"]
        
        font_size = 12
        font_size_axis = 12
        line_width = 2
        font_size_legend = 11
        bbox_to_anchor = (1.25, 1.0)
        plot_type = 'success'
        legend_loc = 'upper right'
        xlabel = 'Overlap threshold'
        ylabel = 'Overlap Precision [%]'
        xlim = (0, 1.0)
        ylim = (0, 100)
        title = 'Success plot - ' + tracker

        matplotlib.rcParams.update({'font.size': font_size})
        matplotlib.rcParams.update({'axes.titlesize': font_size_axis})
        matplotlib.rcParams.update({'axes.titleweight': 'black'})
        matplotlib.rcParams.update({'axes.labelsize': font_size_axis})

        fig, ax = plt.subplots()
        # possible sort according to best auc
        index_sort = auc.argsort(descending=False)

        plotted_lines = []
        legend_text = []

        plot_draw_styles = self._getPlotDrawStyles()

        # tracker variance
        for id, id_sort in enumerate(index_sort):
            disp_name = tracker_names[id_sort]
            legend_text.append(disp_name + " variance")

            line = ax.plot(threshold_set_overlap.tolist(), max_curve[id_sort, :].tolist(), linewidth=line_width, color=plot_draw_styles[id_sort.item()]['color'], linestyle='--')
            plotted_lines.append(line[0])
            line = ax.plot(threshold_set_overlap.tolist(), min_curve[id_sort, :].tolist(), linewidth=line_width, color=plot_draw_styles[id_sort.item()]['color'], linestyle='--')
        # trackers
        for id, id_sort in enumerate(index_sort):
            disp_name = tracker_names[id_sort]
            legend_text.append('{} [{:.1f}]'.format(disp_name, auc[id_sort]))
            
            line = ax.plot(threshold_set_overlap.tolist(), auc_curve[id_sort, :].tolist(), linewidth=line_width, color=plot_draw_styles[id_sort.item()]['color'], linestyle='-')
            plotted_lines.append(line[0])



        ax.legend(plotted_lines[::-1], legend_text[::-1], loc=legend_loc, bbox_to_anchor=bbox_to_anchor, fancybox=False, edgecolor='black', fontsize=font_size_legend, framealpha=1.0)
        ax.set(xlabel=xlabel, ylabel=ylabel, xlim=xlim, ylim=ylim, title=title)
        ax.grid(True, linestyle='-.')
        fig.tight_layout()

        # tikzplotlib.save('{}/{}_plot.tex'.format(result_plot_path, plot_type))
        self.PATH_SUCCESS_PLOT_ALLSEQUENCES_VAR = self.PATH_SUCCESS_PLOT_ALLSEQUENCES_VAR.replace("<TRACKER>", tracker)
        pdf_path = self.PATH_SUCCESS_PLOT_ALLSEQUENCES_VAR + ".pdf"
        fig.savefig(pdf_path, dpi=300, format='pdf', transparent=True)
        plt.draw()
        print("File " + pdf_path + " has been created.")
        # plt.show()




    ################################################################################
    ############################### Precision plots ################################
    ################################################################################
    def createPrecisionPlot(self, tracker: str, seq_number: str):
        """Draws and saves precision plot for given tracker and sequence"""
        self.PATH_CENTER_ERROR_DEFAULT = self.PATH_CENTER_ERROR_DEFAULT.replace("<TRACKER>", tracker).replace("<NUMBER>", seq_number)
        self.PATH_CENTER_ERROR_BORDER = self.PATH_CENTER_ERROR_BORDER.replace("<TRACKER>", tracker).replace("<NUMBER>", seq_number)
        self.PATH_CENTER_ERROR_NFOV = self.PATH_CENTER_ERROR_NFOV.replace("<TRACKER>", tracker).replace("<NUMBER>", seq_number)

        cerror_default = self._parseGivenDataFile(self.PATH_CENTER_ERROR_DEFAULT)
        cerror_border = self._parseGivenDataFile(self.PATH_CENTER_ERROR_BORDER)
        cerror_nfov = self._parseGivenDataFile(self.PATH_CENTER_ERROR_NFOV)

        if len(cerror_default) > 0 and len(cerror_border) > 0 and len(cerror_nfov) > 0:
            threshold_set_center = torch.arange(0, 51, dtype=torch.float64)
            ave_success_rate_plot_center = torch.zeros((3, threshold_set_center.numel()), dtype=torch.float32)
            
            # transform python list to tensors
            cerror_default_tensor = torch.Tensor(cerror_default)
            cerror_border_tensor = torch.Tensor(cerror_border)
            cerror_nfov_tensor = torch.Tensor(cerror_nfov)

            # location error threshold computing
            ave_success_rate_plot_center[0] = (cerror_default_tensor.view(-1, 1) <= threshold_set_center.view(1, -1)).sum(0).float() / len(cerror_default)
            ave_success_rate_plot_center[1] = (cerror_border_tensor.view(-1, 1) <= threshold_set_center.view(1, -1)).sum(0).float() / len(cerror_border)
            ave_success_rate_plot_center[2] = (cerror_nfov_tensor.view(-1, 1) <= threshold_set_center.view(1, -1)).sum(0).float() / len(cerror_nfov)

            # create curves
            prec_curve = ave_success_rate_plot_center * 100.0
            # score should be counted for max 20 pixel error
            prec_score = prec_curve[:, 20]

            precision_plot_opts = {
                'plot_type': 'precision', 
                'legend_loc': 'lower left', 
                'xlabel': 'Location error threshold [pixels]',
                'ylabel': 'Distance Precision [%]', 
                'xlim': (0, 50), 'ylim': (0, 100), 
                'title': 'Precision plot - ' + tracker,
                'font_size_legend': 11
            }
            
            # tracker(modified) names of lines in plot
            tracker_names = [tracker + "-DEFAULT", tracker + "-BORDER", tracker + "-NFOV"]
            
            self.PATH_PRECISION_PLOT = self.PATH_PRECISION_PLOT.replace("<TRACKER>", tracker).replace("<NUMBER>", seq_number)
            self._plotDrawSave(prec_curve, threshold_set_center, prec_score, tracker_names, self._getPlotDrawStyles(), precision_plot_opts, self.PATH_PRECISION_PLOT)


    def createPrecisionPlotAllSequences(self, tracker: str):
        """Draws and saves precision plot for given tracker and all 01-21 video sequences in dataset"""
        threshold_set_center = torch.arange(0, 51, dtype=torch.float64)
        ave_success_rate_plot_center = torch.zeros((len(self.DATASET), 3, threshold_set_center.numel()), dtype=torch.float32)

        for i in range(len(self.DATASET)):
            # load and parse data
            path_default = self.PATH_CENTER_ERROR_DEFAULT.replace("<TRACKER>", tracker).replace("<NUMBER>", self.DATASET[i])
            path_border = self.PATH_CENTER_ERROR_BORDER.replace("<TRACKER>", tracker).replace("<NUMBER>", self.DATASET[i])
            path_nfov = self.PATH_CENTER_ERROR_NFOV.replace("<TRACKER>", tracker).replace("<NUMBER>", self.DATASET[i])
            
            cerror_default = self._parseGivenDataFile(path_default)
            cerror_border = self._parseGivenDataFile(path_border)
            cerror_nfov = self._parseGivenDataFile(path_nfov)

            # transform python lists to tensors
            cerror_default_tensor = torch.Tensor(cerror_default)
            cerror_border_tensor = torch.Tensor(cerror_border)
            cerror_nfov_tensor = torch.Tensor(cerror_nfov)

            # success computing
            ave_success_rate_plot_center[i,0,:] = (cerror_default_tensor.view(-1, 1) <= threshold_set_center.view(1, -1)).sum(0).float() / len(cerror_default)
            ave_success_rate_plot_center[i,1,:] = (cerror_border_tensor.view(-1, 1) <= threshold_set_center.view(1, -1)).sum(0).float() / len(cerror_border)
            ave_success_rate_plot_center[i,2,:] = (cerror_nfov_tensor.view(-1, 1) <= threshold_set_center.view(1, -1)).sum(0).float() / len(cerror_nfov)

        # create curves
        prec_curve = ave_success_rate_plot_center.mean(0) * 100.0
        # score should be counted for max 20 pixel error
        prec_score = prec_curve[:, 20]

        precision_plot_opts = {
            'plot_type': 'precision', 
            'legend_loc': 'lower right', 
            'xlabel': 'Location error threshold [pixels]',
            'ylabel': 'Distance Precision [%]', 
            'xlim': (0, 50), 'ylim': (0, 100), 
            'title': 'Precision plot - ' + tracker,
            'font_size_legend': 11
        }
        
        # tracker(modified) names of lines in plot
        tracker_names = [tracker + "-DEFAULT", tracker + "-BORDER", tracker + "-NFOV"]
        
        self.PATH_PRECISION_PLOT_ALLSEQUENCES = self.PATH_PRECISION_PLOT_ALLSEQUENCES.replace("<TRACKER>", tracker)
        self._plotDrawSave(prec_curve, threshold_set_center, prec_score, tracker_names, self._getPlotDrawStyles(), precision_plot_opts, self.PATH_PRECISION_PLOT_ALLSEQUENCES)


    def createPrecisionPlotAllTrackersSequence(self, seq_number: str, default=False, border=False, nfov=False):
        """Draws and saves precision plot for all trackers (default/border/nfov) and for given video sequence only"""
        threshold_set_center = torch.arange(0, 51, dtype=torch.float64)
        ave_success_rate_plot_center = torch.zeros((len(self.TRACKERS), threshold_set_center.numel()), dtype=torch.float32)

        path = ""
        save_path = self.PATH_PRECISION_PLOT_ALLTRACKERS_SEQ.replace("<NUMBER>", seq_number)
        tracker_names = self.TRACKERS
        title = "Precision plot"
        if default:
            path = self.PATH_CENTER_ERROR_DEFAULT
            save_path += "-default"
            title += " - DEFAULT"
        elif border:
            path = self.PATH_CENTER_ERROR_BORDER
            save_path += "-border"
            title += " - BORDER"
        elif nfov:
            path = self.PATH_CENTER_ERROR_NFOV
            save_path += "-nfov"
            title += " - NFOV"

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
        
        precision_plot_opts = {
            'plot_type': 'precision', 
            'legend_loc': 'lower right', 
            'xlabel': 'Location error threshold [pixels]',
            'ylabel': 'Distance Precision [%]', 
            'xlim': (0, 50), 'ylim': (0, 100), 
            'title': title + " (Sequence " + seq_number + ")",
            'font_size_legend': 10
        }
        
        self._plotDrawSave(prec_curve, threshold_set_center, prec_score, tracker_names, self._getPlotDrawStyles(), precision_plot_opts, save_path)


    def createPrecisionPlotAllTrackers(self, default=False, border=False, nfov=False):
        """Draws and saves success plot for all trackers (default/border/nfov) and all 01-21 video sequences in dataset"""
        threshold_set_center = torch.arange(0, 51, dtype=torch.float64)
        ave_success_rate_plot_center = torch.zeros((len(self.DATASET), len(self.TRACKERS), threshold_set_center.numel()), dtype=torch.float32)

        path = ""
        save_path = self.PATH_PRECISION_PLOT_ALLTRACKERS
        tracker_names = self.TRACKERS
        title = "Precision plot"
        if default:
            path = self.PATH_CENTER_ERROR_DEFAULT
            save_path += "-default"
            title += " - DEFAULT"
        elif border:
            path = self.PATH_CENTER_ERROR_BORDER
            save_path += "-border"
            title += " - BORDER"
        elif nfov:
            path = self.PATH_CENTER_ERROR_NFOV
            save_path += "-nfov"
            title += " - NFOV"

        for i in range(len(self.DATASET)):
            for j in range(len(self.TRACKERS)):
                # load and parse data
                current_path = path.replace("<TRACKER>", self.TRACKERS[j]).replace("<NUMBER>", self.DATASET[i])
                cerror = self._parseGivenDataFile(current_path)

                # transform python lists to tensors
                cerror_tensor = torch.Tensor(cerror)

                # success computing
                ave_success_rate_plot_center[i,j,:] = (cerror_tensor.view(-1, 1) <= threshold_set_center.view(1, -1)).sum(0).float() / len(cerror)

        # create curves
        prec_curve = ave_success_rate_plot_center.mean(0) * 100.0
        # score should be counted for max 20 pixel error
        prec_score = prec_curve[:, 20]

        precision_plot_opts = {
            'plot_type': 'precision', 
            'legend_loc': 'lower right', 
            'xlabel': 'Location error threshold [pixels]',
            'ylabel': 'Distance Precision [%]', 
            'xlim': (0, 50), 'ylim': (0, 100), 
            'title': title,
            'font_size_legend': 10
        }
        
        self._plotDrawSave(prec_curve, threshold_set_center, prec_score, tracker_names, self._getPlotDrawStyles(), precision_plot_opts, save_path)
