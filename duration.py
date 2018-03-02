import logging
logging.basicConfig(filename='hrmonitorlog.txt', format='%(levelname)s \
%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG)

def duration(filename):
    """module that determines the duration of the ECG input signal

    :param filename: the file name of the ECG input

    :returns duration: duration of signal as a float (sec)
    """
    import pandas as pd
    from import_data import import_data
    df = import_data(filename)
    df.columns = ["time", "voltage"]
    duration = df["time"].max()
    return duration
