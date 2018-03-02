def mean_hr_bpm():
    import pandas as pd
    import numpy as np
    import scipy.signal as signal
    from scipy.signal import savgol_filter
    template = pd.read_csv("test_data/template.csv", header=None)
    val = template.values
    std_template = (val - np.mean(val))


    import matplotlib as mpl
    mpl.use('TkAgg')
    import matplotlib.pyplot as plt



#
    from pathlib import Path
    file_choice = input("Filename (e.g. test_data1.csv): ")
    choice = Path("test_data/"+file_choice)
    #time_choice = input("Time Scale (minutes): ")
    if choice.exists():
        single_df = pd.read_csv("test_data/"+file_choice, header=None)
#
        single_df.columns = ["time","voltage"]
        default_time = single_df["time"]
        values = single_df.values
        std_input = (values - np.mean(values))
        corr = np.correlate(std_input[:,1], std_template[:,1], mode="full")
        #lowpass = np.convolve(corr, np.ones(100), mode="full")
        #filtered = savgol_filter(corr, 3, 1)
        #corr = np.correlate(norm_input[:,1], norm_input[:,1], mode="full")
        peaks = signal.find_peaks_cwt(corr, np.arange(1,260))
        total_beats = len(peaks)
        print(total_beats)
        plt.plot(corr)
        #plt.plot(peaks)
        plt.show()
        #time_array = values[peaks,0]

        #print(time_array)



    else:
        print("You're selection is invalid. Please Choose a file in the \
        test_data folder")
    #if time_choice == None:
        #time_choice = default_time




if __name__ == '__main__':
    mean_hr_bpm()
