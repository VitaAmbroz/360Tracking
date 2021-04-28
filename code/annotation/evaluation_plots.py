#################################################################################################
# Visual object tracking in panoramic video
# Master thesis at Brno University of Technology - Faculty of Information Technology
# Author:       Vít Ambrož (xambro15@stud.fit.vutbr.cz)
# Supervisor:   Doc. Ing. Martin Čadík, Ph.D.
# Module:       evaluation_plots.py
# Description:  TODO
#################################################################################################
# This source code has been inspired by:
# https://github.com/visionml/pytracking/blob/master/pytracking/analysis/plot_results.py
#################################################################################################

import sys
import glob
import os
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import torch


class EvaluationPlots:
    def __init__(self, tracker: str, seq_number: int):
        self.tracker = tracker
        self.seq_number = seq_number

        self.PATH_IOU_DEFAULT = "annotation/results/<TRACKER>/<NUMBER>/<NUMBER>-result-default-iou.txt"
        self.PATH_IOU_BORDER = "annotation/results/<TRACKER>/<NUMBER>/<NUMBER>-result-border-iou.txt"
        self.PATH_IOU_NFOV = "annotation/results/<TRACKER>/<NUMBER>/<NUMBER>-result-nfov-iou.txt"

        self.PATH_IOU_PLOT = "annotation/results/<TRACKER>/<NUMBER>/<NUMBER>-success-plot.pdf"
        self.PATH_IOU_PLOT = self.PATH_IOU_PLOT.replace("<TRACKER>", self.tracker).replace("<NUMBER>", self.seq_number)

    
    def _parseGivenDataFile(self, path):
        dataFile = open(path, 'r')
        lines = dataFile.readlines()

        # init empty iou list
        iouList = []
        # parse lines containing float value of intersection over union
        for line in lines:
            iou = float(line)
            iouList.append(iou)

        return iouList


    def _getPlotDrawStyles(self):
        plot_draw_style = [{'color': (1.0, 0.0, 0.0), 'line_style': '-'},
                        {'color': (0.0, 1.0, 0.0), 'line_style': '-'},
                        {'color': (0.0, 0.0, 1.0), 'line_style': '-'},
                        {'color': (0.0, 0.0, 0.0), 'line_style': '-'},
                        {'color': (1.0, 0.0, 1.0), 'line_style': '-'},
                        {'color': (0.0, 1.0, 1.0), 'line_style': '-'},
                        {'color': (0.5, 0.5, 0.5), 'line_style': '-'},
                        {'color': (136.0 / 255.0, 0.0, 21.0 / 255.0), 'line_style': '-'},
                        {'color': (1.0, 127.0 / 255.0, 39.0 / 255.0), 'line_style': '-'},
                        {'color': (0.0, 162.0 / 255.0, 232.0 / 255.0), 'line_style': '-'},
                        {'color': (0.0, 0.5, 0.0), 'line_style': '-'},
                        {'color': (1.0, 0.5, 0.2), 'line_style': '-'},
                        {'color': (0.1, 0.4, 0.0), 'line_style': '-'},
                        {'color': (0.6, 0.3, 0.9), 'line_style': '-'},
                        {'color': (0.4, 0.7, 0.1), 'line_style': '-'},
                        {'color': (0.2, 0.1, 0.7), 'line_style': '-'},
                        {'color': (0.7, 0.6, 0.2), 'line_style': '-'}]

        return plot_draw_style


    def createPlot(self):
        self.PATH_IOU_DEFAULT = self.PATH_IOU_DEFAULT.replace("<TRACKER>", self.tracker).replace("<NUMBER>", self.seq_number)
        self.PATH_IOU_BORDER = self.PATH_IOU_BORDER.replace("<TRACKER>", self.tracker).replace("<NUMBER>", self.seq_number)
        self.PATH_IOU_NFOV = self.PATH_IOU_NFOV.replace("<TRACKER>", self.tracker).replace("<NUMBER>", self.seq_number)

        iou_default = self._parseGivenDataFile(self.PATH_IOU_DEFAULT)
        iou_border = self._parseGivenDataFile(self.PATH_IOU_BORDER)
        iou_nfov = self._parseGivenDataFile(self.PATH_IOU_NFOV)

        if len(iou_default) > 0 and len(iou_border) > 0 and len(iou_nfov) > 0:
            plot_bin_gap = 0.05
            threshold_set_overlap = torch.arange(0.0, 1.0 + plot_bin_gap, plot_bin_gap, dtype=torch.float64)
            ave_success_rate_plot_overlap = torch.zeros((3, threshold_set_overlap.numel()), dtype=torch.float32)
            
            iou_default_tensor = torch.Tensor(iou_default)
            iou_border_tensor = torch.Tensor(iou_border)
            iou_nfov_tensor = torch.Tensor(iou_nfov)

            # print(iou_default_tensor)
            # print(ave_success_rate_plot_overlap)

            ave_success_rate_plot_overlap[0] = (iou_default_tensor.view(-1, 1) > threshold_set_overlap.view(1, -1)).sum(0).float() / len(iou_default)
            ave_success_rate_plot_overlap[1] = (iou_border_tensor.view(-1, 1) > threshold_set_overlap.view(1, -1)).sum(0).float() / len(iou_border)
            ave_success_rate_plot_overlap[2] = (iou_nfov_tensor.view(-1, 1) > threshold_set_overlap.view(1, -1)).sum(0).float() / len(iou_nfov)

            ave_success_rate_plot_overlap = ave_success_rate_plot_overlap * 100.0

            # compute AUC (area under curve for 3 results/IoU)
            auc1 = ave_success_rate_plot_overlap[0].mean(-1)
            auc2 = ave_success_rate_plot_overlap[1].mean(-1)
            auc3 = ave_success_rate_plot_overlap[2].mean(-1)
            # concatenate to tensor list
            auc = torch.Tensor([auc1, auc2, auc3])

            success_plot_opts = {
                'plot_type': 'success', 
                'legend_loc': 'lower left', 
                'xlabel': 'Overlap threshold',
                'ylabel': 'Overlap Precision [%]', 
                'xlim': (0, 1.0), 'ylim': (0, 100), 
                'title': 'Success plot',
                'font_size_legend': 11
            }
            
            # tracker(modified) names of lines in plot
            tracker_names = [self.tracker + "-DEFAULT", self.tracker + "-BORDER", self.tracker + "-NFOV"]

            self._plot_draw_save(ave_success_rate_plot_overlap, threshold_set_overlap, auc, tracker_names, self._getPlotDrawStyles(), success_plot_opts)

        
    def _plot_draw_save(self, y, x, scores, trackers, plot_draw_styles, plot_opts):
        # Plot settings
        font_size = plot_opts.get('font_size', 12)
        font_size_axis = plot_opts.get('font_size_axis', 13)
        line_width = plot_opts.get('line_width', 2)
        font_size_legend = plot_opts.get('font_size_legend', 13)

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


        ax.legend(plotted_lines[::-1], legend_text[::-1], loc=legend_loc, fancybox=False, edgecolor='black', fontsize=font_size_legend, framealpha=1.0)

        ax.set(xlabel=xlabel, ylabel=ylabel, xlim=xlim, ylim=ylim, title=title)

        ax.grid(True, linestyle='-.')
        fig.tight_layout()

        # tikzplotlib.save('{}/{}_plot.tex'.format(result_plot_path, plot_type))
        fig.savefig(self.PATH_IOU_PLOT, dpi=300, format='pdf', transparent=True)
        plt.draw()
        print("File " + self.PATH_IOU_PLOT + " has been created.")
        # plt.show()