import logging
logging.basicConfig(filename='hrmonitorlog.txt', format='%(levelname)s \
%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG)

def mean_hr_bpm(filename):
    """module to take user input for time scale, and analyze ECG input in \
    that time scale

    :param filename: the name of a file located in the /test_data folder \
    entered as a string

    :returns heartrate: heartrate during a specific period as a float
    :raises IOError: raised if user tries to input value not accepted by \
    program
    :raises ValueError: raised if the generally accepted values fall outside \
    of the signal time range
    """
    import numpy as np
    import pandas as pd
    import scipy.signal as signal
    time_input = input("Please input time (10 sec, 20 sec, or full signal): ")
    from extract_data import extract_time_data
    time_vector = extract_time_data(filename)

    if np.max(time_vector) >= float(time_input[:-4]):
        if str(time_input) == "10" + " sec":
            from extract_data import extract_time_data
            time_vector = extract_time_data(filename)
            a = np.where(time_vector == 10)[0]
            from import_data import import_data
            df = import_data(filename)
            values = df.values
            b = values[np.arange(0,a),1]
            b_norm = b - np.mean(b)
            template = pd.read_csv("test_data/template.csv", header=None)
            from extract_data import extract_template_data
            norm_template = extract_template_data(template)
            corr = np.correlate(norm_template, b_norm, mode="full")
            peaks = signal.find_peaks_cwt(corr, np.arange(1,300))
            heartrate = len(peaks) / (10/60)
        elif str(time_input) == "20" + " sec":
            from extract_data import extract_time_data
            time_vector = extract_time_data(filename)
            a = np.where(time_vector == 20)[0]
            from import_data import import_data
            df = import_data(filename)
            values = df.values
            b = values[np.arange(0,a),1]
            b_norm = b - np.mean(b)
            template = pd.read_csv("test_data/template.csv", header=None)
            from extract_data import extract_template_data
            norm_template = extract_template_data(template)
            corr = np.correlate(norm_template, b_norm, mode="full")
            peaks = signal.find_peaks_cwt(corr, np.arange(1,300))
            heartrate = len(peaks) / (20/60)
        else:
            raise IOError("Invalid input. Try Again (Make sure to include " \
            "sec)")
    else:
        raise ValueError("Attempted input outside signal range")
    return heartrate
