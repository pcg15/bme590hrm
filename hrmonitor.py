import json
import logging
import numpy as np
import pandas as pd
import scipy.signal as signal
from pathlib import Path


logging.basicConfig(filename='hrmonitorlog.txt', format='%(levelname)s \
%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG)


class HRMonitor:

    """
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
        from duration import duration
        duration = duration(self.filename)
        return duration

    def voltage_extremes(self):
        from voltage_extremes import voltage_extremes
        voltage_extremes = voltage_extremes(self.filename)
        return voltage_extremes

    def num_beats(self):
        from num_beats import num_beats
        num_beats = num_beats(self.filename)
        return num_beats

    def beats(self):
        from beats import beats
        beats = beats(self.filename)
        return beats

    def mean_hr_bpm(self):
        from mean_hr_bpm import mean_hr_bpm
        mean_hr_bpm = mean_hr_bpm(self.filename)
        return mean_hr_bpm

    def json_maker(self, filename, attributes):
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
