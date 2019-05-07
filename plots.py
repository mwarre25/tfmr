"""
tfmr.plots
=========================================================
tfmr sub-module for storing tfmr data plotting functions.
"""

import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
import datetime as dt
import os
import re
from pprint import pprint
from win32com.client import Dispatch
# endregion

# region plot stuff
f_size = 16  # global font size
plt.style.use("ggplot")
now = dt.datetime.now().strftime('%Y-%m-%d_%I%M%p').upper()

# need to add the 'merge_left_on' and 'merge_right_on' variables to the other
# plotting code; then need to abstract plotting more


def ndi_dp_plot(ndi,
                dp_table,
                merge_left_on='SERIALNUM',
                merge_right_on='Serial Number',
                plot_dp_type='min',
                f_size=16,
                fig_size=(20, 12),
                plt_col='green',
                plt_title_anno='Testing',
                plt_xlab_anno='Normal Degradation',
                plt_ylab_anno='Degree of Polymerization (min)',
                pnt_labs=0,
                **kwargs):
    """Displays NDI v. DP plot and returns dataframe

    This function takes as input a dataframe containing NDI, another dataframe
    containing DP, aggregates the DP values into min, mean, and max, then joins 
    the NDI and DP table to plot it.

    Most of the arguments are for plot customization.

    Args:
        ndi (dataframe): Dataframe containing at least a serial number and NDI
        dp_table (dataframe): Dataframe containing at least a serial number and DP field 
        merge_left_on (string): Field from left dataframe to join the right dataframe
        merge_right_on (string): Field from right dataframe to join the left dataframe
        plot_dp_type (string): String acting as case for which type of DP aggregate value to use ('min', 'mean', or 'max' currently)
        f_size (int): font size integer for matplotlib
        fig_size (2-tuple of ints): figure size tuple for matplotlib ((width, height) in inches)
        plt_col (string): see https://matplotlib.org/api/colors_api.html
        plt_title_anno (string): Add custom plot title
        plt_xlab_anno (string): Add custom x-label
        plt_ylab_anno (string): Add custom y-label
        pnt_labs (int): This acts as a bool (T/F) to determine if you want to add labels to the markers of the plot
    
    Returns:
        A plot is displayed (might have to adjust how it's displayed for Jupyter notebooks but try it first).
        Also returns the dataframe used for the plot.
        Also saves the dataframe to png in current working directory.
    """
    plt.figure(figsize=fig_size)
    plt.style.use('ggplot')
    plt.gcf()
    plt.xticks(fontsize=f_size, rotation=45)
    plt.yticks(fontsize=f_size)
    plt.axis((0.0, 1.0, 0, 1000))
    plt.tight_layout()
    plt.xlabel(plt_xlab_anno, fontsize=f_size)

    # region get min, mean, median, max DP
    try:
        dp_stats = dp_table.groupby(merge_right_on).DP.agg(
            ['min', 'mean', 'median', 'max']).reset_index().rename(
                columns={
                    'min': 'min_DP',
                    'mean': 'mean_DP',
                    'median': 'median_DP',
                    'max': 'max_DP'
                })
    except Exception as e:
        print('Error in summary stats for dp table: ',
              str(e))  # try/except for debugging
    # endregion

    # region join dp_stats to ndi
    try:  # using pandas merge fn, cleaning up the df
        ndi_dp_df = ndi.merge(dp_stats,
                              how='inner',
                              left_on=merge_left_on,
                              right_on=merge_right_on,
                              suffixes=['', '_y'])
        ndi_dp_df.drop(merge_right_on, axis=1, inplace=True)
        ndi_dp_df.dropna(inplace=True)
        ndi_dp_df.reset_index(drop=True, inplace=True)
    except Exception as e:
        print('Error in ndi|dp_stats merge: ', str(e))
    # endregion

    # region plotting by plot_type
    try:  # the plot fns
        if (plot_dp_type == 'min') and (len(ndi_dp_df.index) !=
                                        0):  # making sure merged df isn't null
            # using min_dp
            plt.plot(ndi_dp_df['NORMALDEGRADATION'],
                     ndi_dp_df['min_DP'],
                     marker='o',
                     linestyle='',
                     color=plt_col,
                     ms=12,
                     label=ndi_dp_df['SERIALNUM'])

            if pnt_labs == 1:
                # labeling points on plot
                for i in range(0, len(ndi_dp_df['NORMALDEGRADATION'])):
                    try:
                        xy = (ndi_dp_df['NORMALDEGRADATION'][i],
                              ndi_dp_df['min_DP'][i])
                        plt.annotate(ndi_dp_df['SERIALNUM'][i],
                                     xy,
                                     fontsize=f_size / 2)
                    except Exception as e:
                        print('Error in labeling: ', str(e))
            else:
                pass

            plt.ylabel(plt_ylab_anno, fontsize=f_size)
            plt.title(
                'Normal Degradation Index v. Degree of Polymerization (min)\n'
                + plt_title_anno,
                fontsize=f_size)
            now = dt.datetime.now().strftime("%d%b%y_%H%M%p").upper()
            try:  # fancy filename saving plot stuff
                pattern = re.compile('([^\s\w]|_)+')
                annot = pattern.sub('',
                                    plt_title_anno).replace('\n', '_').replace(
                                        ' ', '_').lower()
                fname = now + '_NDI_min_DP_' + annot + '.png'
            except Exception as e:
                fname = now + '_NDI_min_DP.png'
            plt.savefig(fname, bbox_inches='tight', dpi=200)
            print(fname + ' plot has been saved to:\n' + os.getcwd())
        elif (plot_dp_type == 'max') and (len(ndi_dp_df.index) != 0):
            plt_ylab_anno = 'Degree of Polymerization (max)'
            plt.plot(ndi_dp_df['NORMALDEGRADATION'],
                     ndi_dp_df['max_DP'],
                     marker='o',
                     color=plt_col,
                     linestyle='',
                     ms=12,
                     label=ndi_dp_df['SERIALNUM'])

            if pnt_labs == 1:
                for i in range(0, len(ndi_dp_df['NORMALDEGRADATION'])):
                    try:
                        xy = (ndi_dp_df['NORMALDEGRADATION'][i],
                              ndi_dp_df['max_DP'][i])
                        plt.annotate(ndi_dp_df['SERIALNUM'][i],
                                     xy,
                                     fontsize=f_size / 2)
                    except Exception as e:
                        print('Error in labeling: ', str(e))
            else:
                pass

            plt.ylabel(plt_ylab_anno, fontsize=f_size)
            plt.title(
                'Normal Degradation v. Degree of Polymerization (max)\n' +
                plt_title_anno,
                fontsize=f_size)
            now = dt.datetime.now().strftime("%d%b%y_%H%M%p").upper()
            try:
                pattern = re.compile('([^\s\w]|_)+')
                annot = pattern.sub('',
                                    plt_title_anno).replace('\n', '_').replace(
                                        ' ', '_').lower()
                fname = now + '_NDI_max_DP_' + annot + '.png'
            except Exception as e:
                fname = now + '_NDI_max_DP.png'
            plt.savefig(fname, bbox_inches='tight', dpi=200)
            print(fname + ' plot has been saved to:\n' + os.getcwd())
        elif (plot_dp_type == 'mean') and (len(ndi_dp_df.index) != 0):
            plt_ylab_anno = 'Degree of Polymerization (mean)'
            plt.plot(ndi_dp_df['NORMALDEGRADATION'],
                     ndi_dp_df['mean_DP'],
                     marker='o',
                     linestyle='',
                     color=plt_col,
                     ms=12,
                     label=ndi_dp_df['SERIALNUM'])

            if pnt_labs == 1:
                for i in range(0, len(ndi_dp_df['NORMALDEGRADATION'])):
                    try:
                        xy = (ndi_dp_df['NORMALDEGRADATION'][i],
                              ndi_dp_df['mean_DP'][i])
                        plt.annotate(ndi_dp_df['SERIALNUM'][i],
                                     xy,
                                     fontsize=f_size / 2)
                    except Exception as e:
                        print('Error in labeling: ', str(e))
            else:
                pass

            plt.ylabel(plt_ylab_anno, fontsize=f_size)
            plt.title(
                'Normal Degradation v. Degree of Polymerization (mean)\n' +
                plt_title_anno,
                fontsize=f_size)
            now = dt.datetime.now().strftime("%d%b%y_%H%M%p").upper()
            try:
                pattern = re.compile('([^\s\w]|_)+')
                annot = pattern.sub('',
                                    plt_title_anno).replace('\n', '_').replace(
                                        ' ', '_').lower()
                fname = now + '_NDI_mean_DP_' + annot + '.png'
            except Exception as e:
                fname = now + '_NDI_mean_DP.png'
            plt.savefig(fname, bbox_inches='tight', dpi=200)
            print(fname + ' plot has been saved to:\n' + os.getcwd())
        else:
            print('merged df is empty!')
            pass
    except Exception as e:
        print('Error in ndi_dp plotting: ', str(e))
    # endregion
    return ndi_dp_df


def furans_dp_plot(f,
                   dp_table,
                   merge_left_on='SERIALNUM',
                   merge_right_on='SERIALNUM',
                   f_size=16,
                   fig_size=(20, 12),
                   plt_col='r',
                   plt_title_anno='Testing',
                   pnt_labs=0,
                   **kwargs):
    """Displays Furans v. DP plot and returns dataframe

    This function takes as input a dataframe containing Furans (2-FAL), another dataframe
    containing DP, aggregates the DP values into min, mean, and max, then joins 
    the NDI and DP table to plot it.

    Most of the arguments are for plot customization.

    Args:
        f (dataframe): Dataframe containing at least a serial number and 2FAL field
        dp_table (dataframe): Dataframe containing at least a serial number and DP field 
        merge_left_on (string): Field from left dataframe to join the right dataframe
        merge_right_on (string): Field from right dataframe to join the left dataframe
        plot_dp_type (string): String acting as case for which type of DP aggregate value to use ('min', 'mean', or 'max' currently)
        f_size (int): font size integer for matplotlib
        fig_size (2-tuple of ints): figure size tuple for matplotlib ((width, height) in inches)
        plt_col (string): see https://matplotlib.org/api/colors_api.html
        plt_title_anno (string): Add custom plot title
        pnt_labs (int): This acts as a bool (T/F) to determine if you want to add labels to the markers of the plot
    
    Returns:
        A plot is displayed (might have to adjust how it's displayed for Jupyter notebooks but try it first).
        Also returns the dataframe used for the plot.
        Also saves the dataframe as png in current working directory.
    """
    plt.figure(figsize=fig_size)
    plt.style.use('ggplot')
    plt.gcf()
    plt.axis((0.0, 10000, 0, 1000))
    plt.xticks(fontsize=f_size, rotation=45)
    plt.yticks(fontsize=f_size)
    plt.tight_layout()
    plt.xlabel('2FAL (ppb)', fontsize=f_size)

    # region get min, mean, median, max DP
    try:
        dp_stats = dp_table.groupby('T-number').DP.agg(
            ['min', 'mean', 'median', 'max']).reset_index().rename(
                columns={
                    'T-number': 'SERIALNUM',
                    'min': 'min_DP',
                    'mean': 'mean_DP',
                    'median': 'median_DP',
                    'max': 'max_DP'
                })
        dp_stats.dropna(inplace=True)
    except Exception as e:
        print('Error in summary stats for dp table: ', str(e))
    # endregion
    # region get min, mean, median, max 2FAL
    try:
        f = f.dropna()
        f.reset_index(drop=True, inplace=True)
        f_stats = f.groupby('SERIALNUM')['2FAL'].agg(
            ['min', 'mean', 'median', 'max']).reset_index().rename(
                columns={
                    'min': 'min_2FAL',
                    'mean': 'mean_2FAL',
                    'median': 'median_2FAL',
                    'max': 'max_2FAL'
                })
    except Exception as e:
        print('Error in summary stats for 2Fal table: ', str(e))
    # endregion
    # region join dp_stats to f_stats
    try:
        f_dp_df = f_stats.merge(dp_stats,
                                how='inner',
                                left_on=f_stats['SERIALNUM'],
                                right_on=dp_stats['SERIALNUM'],
                                suffixes=['', '_y'])
        f_dp_df.drop(['key_0', 'SERIALNUM_y'], axis=1, inplace=True)
    except Exception as e:
        print('Error in f_stats|dp_stats merge: ', str(e))
    # endregion
    # region plotting by plot_type
    try:
        if (len(f_dp_df.index) != 0):
            plt.plot(f_dp_df['max_2FAL'],
                     f_dp_df['min_DP'],
                     marker='o',
                     linestyle='',
                     color=plt_col,
                     ms=12,
                     label=f_dp_df['SERIALNUM'])

            if pnt_labs == 1:
                for i in range(0, len(f_dp_df['max_2FAL'])):
                    try:
                        xy = (f_dp_df['max_2FAL'][i], f_dp_df['min_DP'][i])
                        plt.annotate(f_dp_df['SERIALNUM'][i],
                                     xy,
                                     fontsize=f_size / 2)
                    except Exception as e:
                        print('Error in labeling: ', str(e))
            else:
                pass

            plt.xticks(fontsize=f_size, rotation=45)
            plt.yticks(fontsize=f_size)

            plt.xlabel('Max of 2FAL (ppb)', fontsize=f_size)
            plt.ylabel('Min of DP', fontsize=f_size)
            plt.title('Max of 2FAL v. Min of DP\n' + plt_title_anno,
                      fontsize=f_size)
            now = dt.datetime.now().strftime("%d%b%y_%H%M%p").upper()
            try:
                pattern = re.compile('([^\s\w]|_)+')
                annot = pattern.sub('',
                                    plt_title_anno).replace('\n', '_').replace(
                                        ' ', '_').lower()
                fname = now + '_max_2FAL_min_DP_' + annot + '.png'
            except Exception as e:
                fname = now + '_max_2FAL_min_DP.png'
            plt.savefig(fname, bbox_inches='tight', dpi=200)
            print(fname + ' plot has been saved to:\n' + os.getcwd())
        else:
            print('merged df is empty!')
            pass
    except Exception as e:
        print('Error in 2FAL_dp plotting: ', str(e))
    # endregion
    return f_dp_df


def ndi_2fal_plot(ndi,
                  f,
                  merge_left_on='SERIALNUM',
                  merge_right_on='SERIALNUM',
                  plot_2fal_type='max',
                  f_size=16,
                  fig_size=(20, 12),
                  plt_col='r',
                  plt_title_anno='Testing',
                  pnt_labs=0,
                  **kwargs):
    """Displays NDI v. Furans plot and returns dataframe

    This function takes as input a dataframe containing NDI, another dataframe
    containing Furans (2-FAL), aggregates the Furans (2-FAL) values into min, mean, median, and max, then joins 
    the NDI and Furans (2-FAL) table to plot it.

    Most of the arguments are for plot customization.

    Args:
        ndi (dataframe): Dataframe containing at least a serial number and NDI field
        f (dataframe): Dataframe containing at least a serial number and f field 
        merge_left_on (string): Field from left dataframe to join the right dataframe
        merge_right_on (string): Field from right dataframe to join the left dataframe
        plot_2fal_type (string): String acting as case for which type of 2fal aggregate value to use ('min', 'mean', or 'max' currently)
        f_size (int): font size integer for matplotlib
        fig_size (2-tuple of ints): figure size tuple for matplotlib ((width, height) in inches)
        plt_col (string): see https://matplotlib.org/api/colors_api.html
        plt_title_anno (string): Add custom plot title
        pnt_labs (int): This acts as a bool (T/F) to determine if you want to add labels to the markers of the plot
    
    Returns:
        A plot is displayed (might have to adjust how it's displayed for Jupyter notebooks but try it first).
        Also returns the dataframe used for the plot.
        Also saves the dataframe to png in current working directory.
    """
    plt.figure(figsize=fig_size)
    plt.style.use('ggplot')
    plt.gcf()
    plt.axis((0.0, 1.0, 0, 10000))
    plt.xticks(fontsize=f_size, rotation=45)
    plt.yticks(fontsize=f_size)
    plt.tight_layout()
    plt.xlabel('Normal Degradation Index (NDI)', fontsize=f_size)

    # region get min, mean, median, max, avg 2FAL
    try:
        f = f.dropna()
        f.reset_index(drop=True, inplace=True)
        f_stats = f.groupby('SERIALNUM')['2FAL'].agg(
            ['min', 'mean', 'median', 'max']).reset_index().rename(
                columns={
                    'min': 'min_2FAL',
                    'mean': 'mean_2FAL',
                    'median': 'median_2FAL',
                    'max': 'max_2FAL'
                })
    except Exception as e:
        print('Error in summary stats for 2FAL table: ', str(e))
    # endregion
    # region join f_stats to ndi
    try:
        ndi_f_df = ndi.merge(f_stats,
                             how='inner',
                             left_on=merge_left_on,
                             right_on=merge_right_on,
                             suffixes=['', '_y'])
        ndi_f_df.drop(['key_0', 'SERIALNUM_y'], axis=1, inplace=True)
        ndi_f_df.dropna(inplace=True)
        ndi_f_df.reset_index(drop=True, inplace=True)
    except Exception as e:
        print('Error in ndi|f_stats merge: ', str(e))
    # endregion
    # region plotting by plot_2fal_type
    try:
        if (plot_2fal_type == 'min') and (len(ndi_f_df.index) != 0):
            # using min_2FAL
            plt.plot(ndi_f_df['NORMALDEGRADATION'],
                     ndi_f_df['min_2FAL'],
                     marker='o',
                     linestyle='',
                     color=plt_col,
                     ms=12,
                     label=ndi_f_df['SERIALNUM'])

            if pnt_labs == 1:
                for i in range(0, len(ndi_f_df['NORMALDEGRADATION'])):
                    try:
                        xy = (ndi_f_df['NORMALDEGRADATION'][i],
                              ndi_f_df['min_2FAL'][i])
                        plt.annotate(ndi_f_df['SERIALNUM'][i],
                                     xy,
                                     fontsize=f_size / 2)
                    except Exception as e:
                        print('Error in labeling: ', str(e))
            else:
                pass

            plt.ylabel('Min of 2FAL (ppb)', fontsize=f_size)
            plt.title('Normal Degradation Index (NDI) v. Min of 2FAL\n' +
                      plt_title_anno,
                      fontsize=f_size)
            now = dt.datetime.now().strftime('%Y-%m-%d_%I%M%p').upper()
            try:
                pattern = re.compile('([^\s\w]|_)+')
                annot = pattern.sub('',
                                    plt_title_anno).replace('\n', '_').replace(
                                        ' ', '_').lower()
                fname = now + '_NDI_min_2FAL_' + annot + '.png'
            except Exception as e:
                fname = now + '_NDI_min_2FAL.png'
            plt.savefig(fname, bbox_inches='tight', dpi=200)
            print(fname + ' plot has been saved to:\n' + os.getcwd())
        elif (plot_2fal_type == 'max') and (len(ndi_f_df.index) != 0):
            plt.plot(ndi_f_df['NORMALDEGRADATION'],
                     ndi_f_df['max_2FAL'],
                     marker='o',
                     linestyle='',
                     color=plt_col,
                     ms=12,
                     label=ndi_f_df['SERIALNUM'])

            if pnt_labs == 1:
                for i in range(0, len(ndi_f_df['NORMALDEGRADATION'])):
                    try:
                        xy = (ndi_f_df['NORMALDEGRADATION'][i],
                              ndi_f_df['max_2FAL'][i])
                        plt.annotate(ndi_f_df['SERIALNUM'][i],
                                     xy,
                                     fontsize=f_size / 2)
                    except Exception as e:
                        print('Error in labeling: ', str(e))
            else:
                pass

            plt.ylabel('Max of 2FAL (ppb)', fontsize=f_size)
            plt.title('Normal Degradation Index (NDI) v. Max of 2FAL\n' +
                      plt_title_anno,
                      fontsize=f_size)
            now = dt.datetime.now().strftime('%Y-%m-%d_%I%M%p').upper()
            try:
                pattern = re.compile('([^\s\w]|_)+')
                annot = pattern.sub('',
                                    plt_title_anno).replace('\n', '_').replace(
                                        ' ', '_').lower()
                fname = now + '_NDI_max_2FAL_' + annot + '.png'
            except Exception as e:
                fname = now + '_NDI_max_2FAL.png'
            plt.savefig(fname, bbox_inches='tight', dpi=200)
            print(fname + ' plot has been saved to:\n' + os.getcwd())
        elif (plot_2fal_type == 'mean') and (len(ndi_f_df.index) != 0):
            plt.plot(ndi_f_df['NORMALDEGRADATION'],
                     ndi_f_df['mean_2FAL'],
                     marker='o',
                     linestyle='',
                     color=plt_col,
                     ms=12,
                     label=ndi_f_df['SERIALNUM'])

            if pnt_labs == 1:
                for i in range(0, len(ndi_f_df['NORMALDEGRADATION'])):
                    try:
                        xy = (ndi_f_df['NORMALDEGRADATION'][i],
                              ndi_f_df['mean_2FAL'][i])
                        plt.annotate(ndi_f_df['SERIALNUM'][i],
                                     xy,
                                     fontsize=f_size / 2)
                    except Exception as e:
                        print('Error in labeling: ', str(e))
            else:
                pass

            plt.ylabel('Mean of 2FAL (ppb)', fontsize=f_size)
            plt.title('Normal Degradation Index (NDI) v. Mean of 2FAL\n' +
                      plt_title_anno,
                      fontsize=f_size)
            now = dt.datetime.now().strftime('%Y-%m-%d_%I%M%p').upper()
            try:
                pattern = re.compile('([^\s\w]|_)+')
                annot = pattern.sub('',
                                    plt_title_anno).replace('\n', '_').replace(
                                        ' ', '_').lower()
                fname = now + '_NDI_mean_2FAL_' + annot + '.png'
            except Exception as e:
                fname = now + '_NDI_mean_2FAL.png'
            plt.savefig(fname, bbox_inches='tight', dpi=200)
            print(fname + ' plot has been saved to:\n' + os.getcwd())
        else:
            print('merged df is empty!')
            pass
    except Exception as e:
        print('Error in ndi_2FAL plotting: ', str(e))
    # endregion
    return ndi_f_df