# -*- coding: utf-8 -*-
"""

Histogram alongside with a run chart. 

"""
def histogram_plot():
    # Construct the x series
    x = np.linspace(1, len(raw_data), len(raw_data))

        # We need Mean, Median, Standard Deviation, 95% confidence interval
    # The Mean
    Mean_Series = np.mean(raw_data)*np.ones(len(raw_data))

    # The Median
    Median_Value = np.median(raw_data)

    # The Standard Deviation

    Std_Dev_Value = np.std(raw_data)
    Std_Dev_Series = np.ones(len(raw_data))*Std_Dev_Value
    Std_Dev_Series_plus = Mean_Series+Std_Dev_Series*3
    Std_Dev_Series_minus = Mean_Series+Std_Dev_Series*(-3)
    # The 95% confidence interval

    # Plotting the run chart

    ## create a figure, and a list of axes, with figure size manually defined
    fig, ax = plt.subplots(3, 1, figsize=(12, 36))

    #### handle the first Axes
    ax[0].hist(raw_data)
    ax[0].set_xlabel('Refractive Index')
    ax[0].set_ylabel('Probability Density')
    ##### ax[0].set_title('Histrogram Distribution for RI')

    #### handle the second Axes
    ax[1].plot(x, raw_data)
    ax[1].plot(x, Mean_Series)
    ax[1].plot(x, Std_Dev_Series_plus)
    ax[1].plot(x, Std_Dev_Series_minus)
    ax[1].set_xlabel('Batch Series ($\sigma_i=15$)')
    ax[1].set_ylabel('Refractive Index')
    ax[1].set_title('Run Chart for RI')

    #### handle the third Axes for annotating texts
    ax[2].text(0.4, 0.4, 'Median')
    ax[2].text(0.5,0.4,r'$\sigma_i=15$')
    # ax[2].set_xlabel('Batches')
    #ax[2].set_ylabel('Refractive Index')

    # Save image to file? use the following to save it to current file location.
    # plt.savefig("image.png")

    # Show the plot on screen
    plt.show()


if __name__ == "__main__":
    import numpy as np
    #import pandas as pd    # the panda module is not used here, no need to use it.
    import matplotlib.pyplot as plt
    # Read data from csv file
    file_path = r".\0.0.Data\TestData.csv"

    # raw_data=pd.read_csv(file_path,delimiter=",",usecols=[3])
    raw_data = np.genfromtxt(file_path, delimiter=',',
                            skip_header=1, usecols=(3), dtype=float)
    # x=np.genfromtxt(file_path,delimiter=',',skip_header=1,usecols=(0),dtype=None)
    histogram_plot()
