def import_data():

    """A function that asks for the user to input the filename (e.g. \
    test_data1.csv) for the desired data and converts the data into a DataFrame.

    :param file_choice: a string of the csv filename from user input

    :returns: data from the csv file expressed as a pandas DataFrame
    :raises:
    """

    import pandas as pd
    from pathlib import Path
    file_choice = input("Filename: ")
    c = Path("test_data/"+file_choice)
    if c.exists():
        df = pd.read_csv("test_data/"+file_choice, header=None)

if __name__ == '__main__':
    import_data()
