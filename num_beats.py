import logging
logging.basicConfig(filename='hrmonitorlog.txt', format='%(levelname)s \
%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG)


def num_beats(filename):
    """module to detect and count the number of heart beats in the ECG signal

    :param filename: the name of a file located in the /test_data folder \
    entered as a string

    :returns num_beats: number of heart beats in signal as integer
    """
    import numpy as np
    import scipy.signal as signal
    from signal_processing import signal_processing
    logging.info("num_beats: everything imported")
    corr = signal_processing(filename)
    peaks = signal.find_peaks_cwt(corr, np.arange(1, 300))
    num_beats = len(peaks)
    logging.info("num_beats: num_beats found")
    logging.debug("num_beats="+str(num_beats))
    return num_beats
