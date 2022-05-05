import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def plotter(N, time_series):
    #Plot N vs T
    plt.plot(N, time_series)
    plt.xlabel('epoch')
    plt.ylabel('Time')
    plt.title('epoch vs Time')
    plt.show()

#N is number of epochs for bigger testcase
N = [i*200 for i in range(1, 1000000)]
#N is number of epochs for smaller testcase
n = [i for i in range(50)]
with open('larger_testcase.txt', 'r') as f:
    lines = f.readlines()
    time_series = [float(line.strip()) for line in lines]
    time_series = np.array(time_series)
    time_series = time_series.reshape(len(time_series), 1)
    plotter(N, time_series)

with open('smaller_testcase.txt', 'r') as f:
    lines = f.readlines()
    time_series = [float(line.strip()) for line in lines]
    time_series = np.array(time_series)
    time_series = time_series.reshape(len(time_series), 1)
    plotter(N, time_series)