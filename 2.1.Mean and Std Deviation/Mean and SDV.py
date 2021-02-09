# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 13:01:37 2018

@author: 305011902

This script intends to plot Shewhart chart (AKA I-MR chart) for a series of data
the data is from the Iodine Conc. from year 2016 for product Omnipaque

change log:
2020 Sept 1: change the code into function style, by defining a shewhart() function, and by adding “if __name__ == "__main__":” statement. The purpose this change is to allow for later import in other script.

"""
def shewhart(data, para,u_spec, l_spec, product):

    # 1. Preparation of data to be plotted.

    x = np.linspace(1, data.size, data.size)
    avg = np.ones(data.size)*data.sum()/data.size
    avg2 = np.ones(data.size-1)

    upper_Spec = np.ones(data.size)*u_spec
    lower_Spec = np.ones(data.size)*l_spec

    # now i need to calculate the control limit for individual chart, for that i need to calculate the standard deviatio first

    std = np.std(data)

    upper_limit = avg+3*std
    lower_limit = avg-3*std

    # end of the SD calculation

    # to calculate the deviation (the MR part)
    a = []

    for i in range(data.size):
        if i == data.size-1:
            break
        else:
            a.append(abs(data[i+1]-data[i]))

    deviation = np.asarray(a)  # convert the list into a numpy array
    mr_std = np.std(deviation)
    mr_std_upper = 3*mr_std
    mr_average = deviation.sum()/deviation.size
    mr_upper_limit = mr_average + avg2*mr_std_upper # + 3 sigma series
    
    if mr_average - mr_std_upper <= 0:
        mr_lower_limit = avg2*0
    else:
        mr_lower_limit = mr_average - avg2*mr_std_upper
    mr_average_line = avg2*mr_average # average series
    deviationx = np.linspace(1, deviation.size, deviation.size) # create a numpy array for x axis

    # 1. End of data preparation.


    # Now plotting data onto charts

    fig, (ax0, ax1) = plt.subplots(
        nrows=2, ncols=1, sharex=False, figsize=(10, 10))
    fig.suptitle('2020 I-MR chart for '+para + ' of ' + product,
                fontsize=14, fontweight='bold')

    # plot individual data agaist batches
    ax0.plot(x, data, label= para)
    ax0.plot(x, avg, label='Average')  # plot average line
    ax0.plot(x,upper_Spec, label='Upper Spec',color='red')
    ax0.plot(x,lower_Spec, label='Lower Spec',color='red')

    ax0.plot(x, upper_limit, label='+ 3 $\sigma$ deviation', color='orange')
    ax0.plot(x, lower_limit, label='- 3 $\sigma$ deviation', color='orange')

    ax0.legend().set_visible(True)


    ax0.set_title('Individual Chart for ' + para)
    # ax0.set_ylim([1.4547,1.4567]) #setting y limits, does not seem to work

    ax0.set_xlabel('Batches')  # customise the x axis label with batches
    # customise the y axis label with Iodine Conc.
    ax0.set_ylabel(para)

    # The following Moving Range chart

    ax1.plot(deviationx, deviation)
    ax1.plot(deviationx, mr_average_line, label = 'Average MR')
    ax1.plot(deviationx, mr_upper_limit, label = '+ 3 $\sigma$ MR')
    ax1.plot(deviationx, mr_lower_limit, label = '- 3 $\sigma$ MR')

    ax1.legend().set_visible(True)

    ax1.set_title('Moving Range Chart for ' + para)
    ax1.set_xlabel('Moving Ranges')
    # ax1.set_ylim([1.4547,1.4567]) #setting y limits, does not seem to work

    #ax1.set_xlabel('Batches')  # customise the x axis label with batches
    # customise the y axis label with Iodine Conc.
    ax1.set_ylabel('MR of ' + para)

    # fig.show()
    plt.show()
    fig.savefig(r'C:\Python\Projects and Scripts\Statistics\Chemometrics\4.6.Shewhart Charts\Iodine Conc. I-MR chart.jpg',transparent=False, dpi=800,bbox_inches="tight")

if __name__ == "__main__":
    import numpy as np
    import matplotlib.pyplot as plt

    data = np.genfromtxt(r".\0.0.Data\TestData.csv",
                        delimiter=",", skip_header=1, usecols = 3)
    para = 'Water Content (w/w%)'

    u_spec = 4.0
    l_spec = 0.0
    product = 'Iodixanol'

    shewhart(data, para,u_spec, l_spec, product)