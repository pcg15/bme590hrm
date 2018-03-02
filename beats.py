def beats(filename):
    import numpy as np
    import scipy.signal as signal
    from signal_processing import signal_processing
    from extract_data import extract_time_data
    time = extract_time_data(filename)
    corr = signal_processing(filename)
    peaks = signal.find_peaks_cwt(corr, np.arange(1,300))
    approx_time = peaks / 1000
    beats = approx_time
    return beats
