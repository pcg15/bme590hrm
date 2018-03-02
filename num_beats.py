def num_beats(filename):
    import numpy as np
    import scipy.signal as signal
    from signal_processing import signal_processing
    corr = signal_processing(filename)
    peaks = signal.find_peaks_cwt(corr, np.arange(1,300))
    num_beats = len(peaks)
    return num_beats
