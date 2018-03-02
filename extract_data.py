import logging
logging.basicConfig(filename='hrmonitorlog.txt', format='%(levelname)s \
%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG)

def extract_voltage_data(filename):
    """pulls voltage data out of pandas data frame and normalizes values

    :param filename: the name of a file located in the /test_data folder \
    entered as a string

    :returns norm_voltage: normalized voltage data
    """
    import numpy as np
    from import_data import import_data
    df = import_data(filename)
    values = df.values
    voltage = values[:,1]
    norm_voltage = voltage - np.mean(voltage)
    logging.info("extract_voltage_data: norm_voltage found")
    logging.debug("norm_voltage="+str(norm_voltage))
    return norm_voltage

def extract_time_data(filename):
    """pulls time data out of pandas data frame from ECG input

    :param filename: the name of a file located in the /test_data folder \
    entered as a string

    :returns time: array of time values from ECG input
    """
    from import_data import import_data
    df = import_data(filename)
    values = df.values
    time = values[:,0]
    logging.info("extract_time_data: time data found")
    logging.debug("time="+str(time))
    return time

def extract_template_data(template):
    """pulls ECG template data out of pandas data frame and normalizes values

    :param filename: the name of a file located in the /test_data folder \
    entered as a string

    :returns norm_template: normalized template data
    """
    import numpy as np
    temp_values = template.values
    temp_vol = temp_values[:,1]
    norm_template = temp_vol - np.mean(temp_vol)
    logging.info("extract_template_data: norm_template found")
    logging.debug("norm_template="+str(norm_template))
    return norm_template
