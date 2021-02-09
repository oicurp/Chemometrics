# -*- coding: utf-8 -*-
"""
Created on 09 Feb 2021

@author: Renhuan Danny Huang

A simple script for Mean and Standard deviation calculation

"""
def do_mean_std(data, para, product):

    # 1. Preparation of data to be plotted.

    avg = data.sum()/data.size
    std = data.std()

    fig, ax0 = plt.subplots(
        nrows=1, ncols=1, sharex=False, figsize=(10, 10))
    fig.suptitle('Mean and Standard Deivation for '+para + ' of ' + product,
                fontsize=14, fontweight='bold')

    ax0.text(0.05,0.9, 'Mean: ' + str(round(avg,5)) , fontsize=15, color = 'green')
    ax0.text(0.05,0.8, 'Standard Deviation: ' + str(round(std,5)) , fontsize=15, color = 'green')

    ax0.set_title('Meand and Standard Deviation for ' + para)
    
    plt.show()
    fig.savefig(r'.\2.1.Mean and Std Deviation\Mean and Std.jpg',transparent=False, dpi=100,bbox_inches="tight")

if __name__ == "__main__":
    import numpy as np
    import matplotlib.pyplot as plt

    data = np.genfromtxt(r".\0.0.Data\TestData.csv",
                        delimiter=",", skip_header=1, usecols = 3)
    para = 'Water Content (w/w%)'
    product = 'Iodixanol'
    do_mean_std(data, para, product)
    