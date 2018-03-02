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

    def __init__(self, filename="test_data1.csv"):
        self.filename = filename
        self.duration = None
        self.Duration()
        self.voltage_extremes = None
        self.Voltage_extremes()
        self.num_beats = None
        self.Num_beats()
        self.beats = None
        self.Beats()
        self.mean_hr_bpm = None
        self.Mean_hr_bpm()

    def Duration(self):
        """imports duration module to assign duration attribute to class

        :param filename: the name of a file located in the /test_data folder \
        entered as a string

        :returns duration: duration of signal as a float (sec)
        """
        try:
            from duration import duration
            logging.info("HRMonitor: duration imported")
        except:
            print("ImportError:")
            print("duration function could not be found")
        try:
            self.duration = duration(self.filename)
            logging.info("HRMonitor: duration found")
        except TypeError:
            logging.warning("Invalid input type")
            print("TypeError:")
            print("Your input is not supported. Follow tips in parentheses")
        except ValueError:
            logging.warning("Invalid input value")
            print("ValueError")
            print("Your input is not supported. Follow tips in parentheses")
        return duration

    def Voltage_extremes(self):
        """imports voltage_extremes module to assign voltage_extremes \
        attribute to class

        :param filename: the name of a file located in the /test_data folder \
        entered as a string

        :returns voltage_extremes: lead voltage minimum and maximum as tuple \
        (mV)
        """
        try:
            from voltage_extremes import voltage_extremes
            logging.info("HRMonitor: voltage_extremes imported")
        except:
            print("ImportError:")
            print("voltage_extremes function could not be found")
        try:
            self.voltage_extremes = voltage_extremes(self.filename)
            logging.info("HRMonitor: voltage_extremes found")
        except TypeError:
            logging.warning("Invalid input type")
            print("TypeError:")
            print("Your input is not supported. Follow tips in parentheses")
        except ValueError:
            logging.warning("Invalid input value")
            print("ValueError")
            print("Your input is not supported. Follow tips in parentheses")
        return voltage_extremes

    def Num_beats(self):
        """imports num_beats module to assign num_beats attribute to class

        :param filename: the name of a file located in the /test_data folder \
        entered as a string

        :returns num_beats: number of heart beats in signal as integer
        """
        try:
            from num_beats import num_beats
            logging.info("HRMonitor: num_beats imported")
        except:
            print("ImportError:")
            print("num_beats function could not be found")
        try:
            self.num_beats = num_beats(self.filename)
            logging.info("HRMonitor: num_beats found")
        except TypeError:
            logging.warning("Invalid input type")
            print("TypeError:")
            print("Your input is not supported. Follow tips in parentheses")
        except ValueError:
            logging.warning("Invalid input value")
            print("ValueError")
            print("Your input is not supported. Follow tips in parentheses")
        return num_beats

    def Beats(self):
        """imports beats module to assign beats attribute to class

        :param filename: the name of a file located in the /test_data folder \
        entered as a string

        :returns beats: numpy array of times where a heart beat occured
        """
        try:
            from beats import beats
            logging.info("HRMonitor: beats imported")
        except:
            print("ImportError:")
            print("beats function could not be found")
        try:
            self.beats = beats(self.filename)
            logging.info("HRMonitor: beats found")
        except TypeError:
            logging.warning("Invalid input type")
            print("TypeError:")
            print("Your input is not supported. Follow tips in parentheses")
        except ValueError:
            logging.warning("Invalid input value")
            print("ValueError")
            print("Your input is not supported. Follow tips in parentheses")
        return beats

    def Mean_hr_bpm(self):
        """imports mean_hr_bpm module to assign mean_hr_bpm attribute to class

        :param filename: the name of a file located in the /test_data folder \
        entered as a string

        :returns mean_hr_bpm: heartrate during a specific period as a float
        """
        try:
            from mean_hr_bpm import mean_hr_bpm
            logging.info("HRMonitor: mean_hr_bpm imported")
        except:
            print("ImportError:")
            print("mean_hr_bpm function could not be found")
        try:
            self.mean_hr_bpm = mean_hr_bpm(self.filename)
            logging.info("HRMonitor: mean_hr_bpm found")
        except TypeError:
            logging.warning("Invalid input type")
            print("TypeError:")
            print("Your input is not supported. Follow tips in parentheses")
        except ValueError:
            logging.warning("Invalid input value")
            print("ValueError")
            print("Your input is not supported. Follow tips in parentheses")
        return mean_hr_bpm

    def Json_maker(self):
        """imports json_maker module to create a .json file populated with \
        stats from the ECG input and class-associated attributes

        :param filename: the name of a file located in the /test_data folder \
        entered as a string

        :param attributes: the attributes of the HRMonitor class

        :returns test_data*.json: .json file populated with the data \
        generated from HRMonitor attributes being applied to a ECG .csv input
        """
        try:
            from json_maker import json_maker
            logging.info("HRMonitor: json_maker imported")
        except:
            print("ImportError:")
            print("json_maker function could not be found")
        try:
            make_file = json_maker(self.filename)
            logging.info("HRMonitor: json made")
        except TypeError:
            logging.warning("Invalid input type")
            print("TypeError:")
            print("Your input is not supported. Follow tips in parentheses")
        except ValueError:
            logging.warning("Invalid input value")
            print("ValueError")
            print("Your input is not supported. Follow tips in parentheses")
