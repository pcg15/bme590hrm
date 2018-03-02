def beats():
    import pandas as pd
    import numpy as np
    import scipy.signal as signal
    from scipy.signal import savgol_filter
    import matplotlib as mpl
    mpl.use('TkAgg')
    import matplotlib.pyplot as plt
#import template
    template = pd.read_csv("test_data/template.csv", header=None)
    temp_values = template.values
    temp_vol = temp_values[:,1]
    norm_template = temp_vol - np.mean(temp_vol)
#import tester
    from pathlib import Path
    file_choice = input("Filename (e.g. test_data1.csv): ")
    choice = Path("test_data/"+file_choice)
    if choice.exists():
        single_df = pd.read_csv("test_data/"+file_choice, header=None)
        values = single_df.values
        voltage = values[:,1]
        time = values[:,0]
        norm_voltage = voltage - np.mean(voltage)
        corr = np.correlate(norm_template, norm_voltage, mode="full")
        #filtered = savgol_filter(corr, 13, 3)
        peaks = signal.find_peaks_cwt(corr, np.arange(1,300))
        total_beats = len(peaks)
#heart rate
        max_time = np.max(time)
        max_min = max_time / 60
        total_heartrate = total_beats / max_min
        print(total_heartrate)
        plt.plot(corr)
        plt.show()
    else:
        print("You're selection is invalid. Please Choose a file in the \
        test_data folder")

if __name__ == '__main__':
    beats()
