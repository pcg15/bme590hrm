import logging
logging.basicConfig(filename='hrmonitorlog.txt', format='%(levelname)s \
%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG)


def signal_processing(filename):
    """module to correlate normalized values of template and input ECG data

    :param filename: the name of a file located in the /test_data folder \
    entered as a string

    :returns correlation: the correlation of template and input ECG data
    """
    import numpy as np
    import pandas as pd
    from extract_data import extract_template_data
    from extract_data import extract_voltage_data
    from extract_data import extract_time_data
    from import_data import import_data
    logging.info("signal_processing: everything imported")
    template = pd.read_csv("test_data/template.csv", header=None)
    norm_template = extract_template_data(template)
    norm_voltage = extract_voltage_data(filename)
    correlation = np.correlate(norm_template, norm_voltage, mode="full")
    logging.info("signal_processing: correlation")
    return correlation
