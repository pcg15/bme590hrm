import logging
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
    filename = filename[:-4]
    data = {
        "Average Heart Rate" : str(df.mean_hr_bpm) + " bpm",
        "Minimum and Maximum Lead Voltages" : str(df.voltage_extremes) + " mV",
        "Duration of Signal" : str(df.duration) + " seconds",
        "Number of Beats Detected" : str(df.num_beats) + " beats",
        "Times When a Beat Occured" : str(df.beats)
    }
    with open(str(filechoice)+".json", 'w') as f:
        json.dump(data, f)
