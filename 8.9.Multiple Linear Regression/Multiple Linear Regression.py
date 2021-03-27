# -*- coding: utf-8 -*-
"""
Created on Sun Feb 06 2021

@author: Renhuan Danny Huang

This script intends to plot Linear Regression for a series of data


change log:

N/A

"""


def multiple_linear_regression(predictor_c1, predictor_c2, predictor_c3, response_A1, response_A2,
                           response_A3, response_A4, response_A5, response_A6, para, product, fig_title):
    """
    do a linear regression for a series of data (predictors and responses).
    three charts are produced:
    1. Curve fitting line
    2. Residual plot
    3. Output of critical metrics (e.g., a, b, r, confidance interval)

    """

    # Now plotting data onto charts

    fig, (ax0, ax1, ax2,ax3,ax4,ax5) = plt.subplots(
        nrows=6, ncols=1, sharex=False, figsize=(10, 20))
    #fig.suptitle(fig_title + para + ' of ' + product,
    #             fontsize=14, fontweight='bold')
    # plot fitted line
    ax0.set_title('scatter for A1', fontsize=10)
    ax0.scatter(predictor_c1, response_A1)
    #ax0.plot(data_x, res.intercept + res.slope *
    #         data_x, 'r', label='Fitted Line')
    ax0.legend().set_visible(True)
    #ax0.set_title('Linear Regression for ' + para, fontsize=10)
    # ax0.set_ylim([1.4547,1.4567]) #setting y limits, does not seem to work
    # customise the x axis label with batches
    #ax0.set_xlabel('Concentrations (pg/mL)')
    # customise the y axis label with Iodine Conc.
    #ax0.set_ylabel(para)
    # end of plotting fitted line

    # plot residual chart
    
    ax1.set_title('scatter for A2', fontsize=10)
    ax1.scatter(predictor_c1, response_A2)
    #ax1.plot(data_x, data_zero_line, 'r', label='zero line')

    # end of plotting residual chart

    # calculating and plotting metrics

    ax2.set_title('scatter for A3', fontsize=10)
    ax2.scatter(predictor_c1, response_A3)
    ax3.set_title('scatter for A4', fontsize=10)
    ax3.scatter(predictor_c1, response_A4)
    ax4.set_title('scatter for A5', fontsize=10)
    ax4.scatter(predictor_c1, response_A5)
    ax5.set_title('scatter for A6', fontsize=10)
    ax5.scatter(predictor_c1, response_A6)

   # ax2.text(0.05, 0.6, 'Standard error of the estimated slope: ' +
    #         str(round(res.stderr, 5)), fontsize=10, color='green')
    # ax2.axis('off')
    # ax2.annotate('Standard error of the estimated intercept: ' + str(res.intercept_stderr), xy=(0.05,0.7))

    # end of metrics

    plt.show()
    fig.savefig(r".\8.9.Multiple Linear Regression\Multiple Regression chart.jpg",
                transparent=False, dpi=100, bbox_inches="tight")


if __name__ == "__main__":
    import numpy as np
    import matplotlib.pyplot as plt
    from scipy import stats
"""
    data_x = np.genfromtxt(r".\5.0.Calibration Methods, Regression and Correlation\example data.csv",
                           delimiter = ",", skip_header = 1, usecols = 0)
    data_y = np.genfromtxt(r".\5.0.Calibration Methods, Regression and Correlation\example data.csv",
                           delimiter=",", skip_header=1, usecols=1)
"""
predictor_c1 = [0.89, 0.46, 0.45, 0.56, 0.41, 0.44, 0.34, 0.74, 0.75, 0.48]
predictor_c2 = [0.02, 0.09, 0.16, 0.09, 0.02, 0.17, 0.23, 0.11, 0.01, 0.10]
predictor_c3 = [0.01, 0.24, 0.23, 0.09, 0.28, 0.14, 0.20, 0.01, 0.10, 0.06]
response_A1 = [18.7, 31.3, 30.0, 20.0, 31.5, 22.0, 25.7, 18.7, 27.3, 18.3]
response_A2 = [26.8, 33.4, 35.1, 25.7, 34.8, 28.0, 31.4, 26.8, 34.6, 22.8]
response_A3 = [42.1, 45.7, 48.3, 39.3, 46.5, 38.5, 41.1, 37.8, 47.8, 32.8]
response_A4 = [56.6, 49.3, 53.5, 46.6, 46.7, 46.7, 50.6, 50.6, 55.9, 43.4]
response_A5 = [70.0, 53.8, 59.2, 56.5, 48.5, 54.1, 53.5, 65.0, 67.9, 49.6]
response_A6 = [83.2, 55.3, 57.7, 57.8, 51.1, 53.6, 49.3, 72.3, 75.2, 51.1]

para = 'Absorbance (AU)'
product = 'an Unknown Sample'
fig_title = 'Multiple Linear Regression for Assay by UV-Vis'

multiple_linear_regression(predictor_c1, predictor_c2, predictor_c3, response_A1, response_A2,
                           response_A3, response_A4, response_A5, response_A6, para, product, fig_title)
