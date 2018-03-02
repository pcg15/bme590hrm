import logging
from duration import duration
from mean_hr_bpm import mean_hr_bpm
from num_beats import num_beats
from beats import beats
from voltage_extremes import voltage_extremes as ve
logging.basicConfig(filename='hrmonitorlog.txt', format='%(levelname)s \
%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG)


def json_maker(filename):
    """module that creates a .json file populated with \
    stats from the ECG input and class-associated attributes

    :param filename: the name of a file located in the /test_data folder \
    entered as a string

    :param attributes: the attributes of the HRMonitor class

    :returns test_data*.json: .json file populated with the data \
    generated from HRMonitor attributes being applied to a ECG .csv input
    """
    import json
    filechoice = filename[:-4]
    data = {
        "Duration of Signal": str(duration(filename)) + " seconds",
        "Minimum and Maximum Lead Voltages": str(ve(filename)) + " mV",
        "Number of Beats Detected": str(num_beats(filename)) + " beats",
        "Times When a Beat Occured": str(beats(filename)),
        "Average Heart Rate": str(mean_hr_bpm(filename)) + " bpm"
    }
    with open(str(filechoice)+".json", 'w') as f:
        json.dump(data, f)
