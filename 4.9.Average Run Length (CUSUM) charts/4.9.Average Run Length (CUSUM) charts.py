# -*- coding: utf-8 -*-
"""
 
This script is to produce a Cumulative SUM chart, which provides the capability to detect a change in process mean. The Cumsum chart
highlights its capability in speedy detection of mean change.

Definitions: 
    ARL = Average Run Length.

Author = HRH

Change Log 2020\09\01 : change the style from structure flow into function flow, to allow import from other script in the future.

"""


def cusum(para, raw_data):
    # Construct the x series
    x = np.linspace(1, len(raw_data), len(raw_data))

    # Now the calculation for all the parameters in a Descriptive Statistics

    # We need Mean, Median, Standard Deviation, 95% confidence interval
    # The Mean
    Mean_Series = np.mean(raw_data)*np.ones(len(raw_data))

    diff_sample_mean = raw_data - Mean_Series
    #now calculate a CUSUM series
    CUSUM = []
    

    for i in range(len(diff_sample_mean)):
        cusum_element = 0
        for j in range(i+1):
            cusum_element += diff_sample_mean[j]
        CUSUM.append(cusum_element)
    #print(diff_sample_mean[0:4])
    #print(CUSUM[0:4])
    cusum_x = np.linspace(1, len(CUSUM), len(CUSUM))
    # The Standard Deviation

    #Std_Dev_Value = np.std(raw_data)
    #Std_Dev_Series = np.ones(len(raw_data))*Std_Dev_Value
    #Std_Dev_Series_plus = Mean_Series+Std_Dev_Series*3
    #Std_Dev_Series_minus = Mean_Series+Std_Dev_Series*(-3)
    # The 95% confidence interval

    # Plotting the run chart

    # create a figure, and a list of axes, with figure size manually defined
    fig, ax = plt.subplots(3, 1, figsize=(50, 100))

    # handle the first Axes, the CUSUM chart
    ax[0].plot(x, Mean_Series, label='Sample Mean', color='green')
    ax[0].plot(x, raw_data, label='Observations', color='pink')

    ax[0].set_xlabel('Sample Number')
    ax[0].set_ylabel(para)

    ax[0].legend().set_visible(True)
    ##### ax[0].set_title('Histrogram Distribution for RI')

    # handle the second Axes, the V-Mask chart
    ax[1].plot(cusum_x, CUSUM, label = 'CUSUM', color ='red', marker = 'o')
    
    #ax[1].plot(x, Mean_Series)
    #ax[1].plot(x, Std_Dev_Series_plus)
    #ax[1].plot(x, Std_Dev_Series_minus)
    ax[1].set_xlabel('Sample Label')
    ax[1].set_yticks([-0.01, 0,0.01], minor = True)
    ax[1].grid(which = 'major', color ='r')
    ax[1].set_ylabel('CUSUM')
    #ax[1].set_title('CUSUM Chart for RI')
    ax[1].legend().set_visible(True)

    # handle the third Axes for annotating texts
    ax[2].text(0.4, 0.4, 'Median')
    ax[2].text(0.5, 0.4, r'$\sigma_i=15$')
    # ax[2].set_xlabel('Batches')
    # ax[2].set_ylabel('Refractive Index')

    # Save image to file? use the following to save it to current file location.
    # plt.savefig("image.png")

    # Show the plot on screen
    plt.show()
    fig.savefig(r'C:\Python\Projects and Scripts\Statistics\Chemometrics\4.9.Average Run Length (CUSUM) charts\Cusum for water content.jpg',transparent=False, dpi=800,bbox_inches="tight")


if __name__ == "__main__":
    import numpy as np
    # import pandas as pd    # the panda module is not used here, no need to use it.
    import matplotlib.pyplot as plt
    # Read data from csv file
    file_path = r".\0.0.Data\TestData.csv"
    raw_data = np.genfromtxt(file_path, delimiter=',',
                             skip_header=1, usecols=(3), dtype=float)
    # x=np.genfromtxt(file_path,delimiter=',',skip_header=1,usecols=(0),dtype=None)
    average_run_length = 3
    para = 'Water Content'
    cusum(para, raw_data)
