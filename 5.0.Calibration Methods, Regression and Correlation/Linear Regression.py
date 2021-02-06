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

    fig, (ax0,ax1,ax2) = plt.subplots(nrows=3, ncols=1, sharex=False, figsize=(10, 10))
    fig.suptitle(fig_title +para + ' of ' + product,
                fontsize=14, fontweight='bold')
    # plot fitted line
    ax0.plot(data_x, data_y, 'o', label= para)
    ax0.plot(data_x, res.intercept + res.slope*data_x, 'r', label= 'Fitted Line')
    ax0.legend().set_visible(True)
    ax0.set_title('Linear Regression for ' + para, fontsize = 15)
    # ax0.set_ylim([1.4547,1.4567]) #setting y limits, does not seem to work
    ax0.set_xlabel('Concentrations (pg/mL)')  # customise the x axis label with batches
    # customise the y axis label with Iodine Conc.
    ax0.set_ylabel(para)
    # end of plotting fitted line

    # plot residual chart
    data_residual = data_y - (data_x*res.slope + res.intercept)
    data_zero_line = data_x*0

    ax1.set_title('Residual Plot',fontsize = 15)
    ax1.plot(data_x, data_residual, 'o', label= 'residual of y')
    ax1.plot(data_x, data_zero_line, 'r', label= 'zero line')

    # end of plotting residual chart

    ax2.set_title('Regression Results',fontsize = 15)
    ax2.text(0.05,0.9, 'Regression Formula: ' + 'y= ' + str(round(res.intercept,5)) + '+ ' + str(round(res.slope,5)) + 'x', fontsize=15, color = 'green')
    #ax2.annotate('Regression formula: ' + 'y= ' + str(round(res.intercept,5)) + '+ ' + str(round(res.slope,5)) + 'x', xy=(0.05,0.9))
    ax2.text(0.05, 0.8, 'Correlation Coefficient (r): ' + str(round(res.rvalue,5)), fontsize = 15, color = 'green')
    ax2.text(0.05, 0.7, 'p for Regression (p): ' + str(res.pvalue), fontsize = 15, color = 'green')
    ax2.text(0.05, 0.6, 'Standard error of the estimated slope: ' + str(round(res.stderr,5)), fontsize = 15, color = 'green')
    #ax2.axis('off')
    #ax2.annotate('Standard error of the estimated intercept: ' + str(res.intercept_stderr), xy=(0.05,0.7))
    
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