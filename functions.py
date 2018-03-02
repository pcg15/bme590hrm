def main():
    """HRMonitor with the following functionalities: time duration in \
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
    duration(filename)
    voltage_extremes(filename)
    num_beats(filename)
    beats(filename)
    user_int = input("Please input time (10 sec or 20 sec): ")
    mean_hr_bpm(filename)
    json_maker(filename)


def duration(filename):
    """imports duration module to calculate duration of signal

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
    print(duration)
    return duration


def voltage_extremes(filename):
    """imports voltage_extremes module to calculate maximum and minimum lead \
    voltages

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
    print(voltage_extremes)
    return voltage_extremes


def num_beats(filename):
    """imports num_beats module to calculate heart beats in sample

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
    print(num_beats)
    return num_beats


def beats(filename):
    """imports beats module to find beat locations (time values)

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
    print(beats)
    return beats


def mean_hr_bpm(filename):
    """imports mean_hr_bpm module to calculate mean heart rate at a user-\
    specified interval

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
    print(heartrate)
    return heartrate


def json_maker(filename):
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


if __name__ == '__main__':
    main()
