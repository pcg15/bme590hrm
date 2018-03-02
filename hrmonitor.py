import json
import logging
import numpy as np
import pandas as pd
import scipy.signal as signal
from pathlib import Path


logging.basicConfig(filename='hrmonitorlog.txt', format='%(levelname)s \
%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG)


class HRMonitor:

    """HRMonitor object with the following attributes: time duration in \
    seconds, lead voltage extremes in mV, the number of heart beats in the \
    signal, an array of times in which the heart beats occured, and the mean \
    heart rate over a user-specified time period; a .json file is also \
    produced populated with the resulting data.

    :param filename: the name of a file located in the /test_data folder \
    entered as a string

    :returns duration: duration of signal as a float (sec)
    :returns voltage_extremes: lead voltage minimum and maximum as tuple (mV)
    :returns num_beats: number of heart beats in signal as integer
    :returns beats: numpy array of times where a heart beat occured
    :returns mean_hr_bpm: heartrate during a specific period as a float
    """

    def __init__(self, filename = "test_data1.csv"):
        self.filename = filename
        self.duration = None
        self.voltage_extremes = None
        self.num_beats = None
        self.beats = None
        self.mean_hr_bpm = None
        self.json_maker = None
        self.main()


    def duration(self):
        """imports duration module to assign duration attribute to class

        :param filename: the name of a file located in the /test_data folder \
        entered as a string

        :returns duration: duration of signal as a float (sec)
        """
        from duration import duration
        duration = duration(self.filename)
        return duration

    def voltage_extremes(self):
        """imports voltage_extremes module to assign voltage_extremes \
        attribute to class

        :param filename: the name of a file located in the /test_data folder \
        entered as a string

        :returns voltage_extremes: lead voltage minimum and maximum as tuple \
        (mV)
        """
        from voltage_extremes import voltage_extremes
        voltage_extremes = voltage_extremes(self.filename)
        return voltage_extremes

    def num_beats(self):
        """imports num_beats module to assign num_beats attribute to class

        :param filename: the name of a file located in the /test_data folder \
        entered as a string

        :returns num_beats: number of heart beats in signal as integer
        """
        from num_beats import num_beats
        num_beats = num_beats(self.filename)
        return num_beats

    def beats(self):
        """imports beats module to assign beats attribute to class

        :param filename: the name of a file located in the /test_data folder \
        entered as a string

        :returns beats: numpy array of times where a heart beat occured
        """
        from beats import beats
        beats = beats(self.filename)
        return beats

    def mean_hr_bpm(self):
        """imports mean_hr_bpm module to assign mean_hr_bpm attribute to class

        :param filename: the name of a file located in the /test_data folder \
        entered as a string

        :returns mean_hr_bpm: heartrate during a specific period as a float
        """
        from mean_hr_bpm import mean_hr_bpm
        mean_hr_bpm = mean_hr_bpm(self.filename)
        return mean_hr_bpm

    def json_maker(self, filename, attributes):
        """imports json_maker module to create a .json file populated with \
        stats from the ECG input and class-associated attributes

        :param filename: the name of a file located in the /test_data folder \
        entered as a string

        :param attributes: the attributes of the HRMonitor class

        :returns test_data*.json: .json file populated with the data \
        generated from HRMonitor attributes being applied to a ECG .csv input
        """
        from json_maker import json_maker
        make_file = json_maker(self.filename)

    def main(self.filename):
        self.duration = self.duration(self.filename)
        self.voltage_extremes = self.voltage_extremes(self.filename)
        self.num_beats = self.num_beats(self.filename)
        self.beats = self.beats(self.filename)
        self.mean_hr_bpm = self.mean_hr_bpm(self.filename)
        self.json_maker()

if __name__ == "__main__":
    a = HRMonitor(filename='test_data1.csv')
