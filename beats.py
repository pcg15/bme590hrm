import logging
logging.basicConfig(filename='hrmonitorlog.txt', format='%(levelname)s \
%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG)

def beats(filename):
    """module that detects the number of heartbeats in an ECG signal

    :param filename: the file name of the ECG input

    :returns beats: numpy array of times where a heart beat occured
    """
    import numpy as np
    import scipy.signal as signal
    from signal_processing import signal_processing
    from extract_data import extract_time_data
    logging.info("beats: everything imported")
    time = extract_time_data(filename)
    corr = signal_processing(filename)
    peaks = signal.find_peaks_cwt(corr, np.arange(1,300))
    approx_time = peaks / 1000
    beats = approx_time
    logging.info("beats: beats found")
    logging.debug("beats="+str(beats))
    return beats
