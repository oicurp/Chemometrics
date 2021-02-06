# -*- coding: utf-8 -*-
"""
Created on Sun Feb 06 2021

@author: Renhuan Danny Huang

This script intends to plot Linear Regression for a series of data


change log:

N/A

"""

def linear_regression(data_x, data_y, para, product, fig_title):

    res = stats.linregress(data_x, data_y)
    # Now plotting data onto charts

    fig, (ax0,ax1) = plt.subplots(nrows=2, ncols=1, sharex=False, figsize=(10, 10))
    fig.suptitle(fig_title +para + ' of ' + product,
                fontsize=14, fontweight='bold')
    # plot individual data agaist batches
    ax0.plot(data_x, data_y, 'o', label= para)
    ax0.plot(data_x, res.intercept + res.slope*data_x, 'r', label= 'Fitted Line')
    ax0.legend().set_visible(True)
    ax0.set_title('Linear Regression for ' + para)
    # ax0.set_ylim([1.4547,1.4567]) #setting y limits, does not seem to work
    ax0.set_xlabel('Concentrations (pg/mL)')  # customise the x axis label with batches
    # customise the y axis label with Iodine Conc.
    ax0.set_ylabel(para)
    
    ax1.set_title('Regression Results')
    ax1.annotate('Regression formula: ' + 'y= ' + str(res.intercept) + '+ ' + str(res.slope) + 'x', xy=(0.05,0.9))
    ax1.annotate('Correlation Coefficient (r): ' + str(res.rvalue), xy=(0.05,0.85))
    ax1.annotate('p for Regression (p): ' + str(res.pvalue), xy=(0.05,0.8))
    ax1.annotate('Standard error of the estimated slope: ' + str(res.stderr), xy=(0.05,0.75))
    #ax1.annotate('Standard error of the estimated intercept: ' + str(res.intercept_stderr), xy=(0.05,0.7))
    
    plt.show()
    fig.savefig(r".\5.0.Calibration Methods, Regression and Correlation\Regression chart.jpg",transparent=False, dpi=100,bbox_inches="tight")

if __name__ == "__main__":
    import numpy as np
    import matplotlib.pyplot as plt
    from scipy import stats

    data_x = np.genfromtxt(r".\5.0.Calibration Methods, Regression and Correlation\example data.csv",
                        delimiter=",", skip_header=1, usecols = 0)
    data_y = np.genfromtxt(r".\5.0.Calibration Methods, Regression and Correlation\example data.csv",
                        delimiter=",", skip_header=1, usecols = 1)
    para = 'Intensity (AU)'
    product = 'Methamphetamine'
    fig_title = 'Linear Regression for Assay by ICP-AES'

    linear_regression(data_x, data_y, para, product, fig_title)