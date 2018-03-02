import logging
logging.basicConfig(filename='hrmonitorlog.txt', format='%(levelname)s \
%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG)

def import_data(filename):
    """a module that asks for the user to input the filename (e.g. \
    test_data1.csv) for the desired data and converts the data into a \
    DataFrame.

    :param filename: a string of the csv filename from user input

    :returns df: data from the csv file expressed as a pandas DataFrame
    :raises IOError: raised if user tries to input a string that is not in \
    the /test_data folder
    """

    import pandas as pd
    from pathlib import Path
    choice = Path("test_data/"+filename)
    if choice.exists():
        df = pd.read_csv("test_data/" + filename, header=None)
    else:
        raise IOError("Invalid Selection: file not in folder")
    return df
