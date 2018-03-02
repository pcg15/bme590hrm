import logging
logging.basicConfig(filename='hrmonitorlog.txt', format='%(levelname)s \
%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG)

def voltage_extremes(filename):
    """module to calculate the maximum and minimum lead voltages of the input \
    ECG data

    :param filename: the name of a file located in the /test_data folder \
    entered as a string

    :returns voltage_extremes: lead voltage minimum and maximum as tuple \
    (mV)
    """
    import pandas as pd
    from import_data import import_data
    df = import_data(filename)
    df.columns = ["time", "voltage"]
    voltage_min = df["voltage"].min()
    voltage_max = df["voltage"].max()
    voltage_extremes = (voltage_min, voltage_max)
    logging.info("voltage_extremes: voltage_extremes found")
    logging.debug("voltage_extremes="+str(voltage_extremes))
    return voltage_extremes
