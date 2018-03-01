def main():
    import_data()
    read_csv()

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
    choice = Path("test_data/"+file_choice)
    if choice.exists():
        single_df = pd.read_csv("test_data/"+file_choice, header=None)
    return single_df

def import_multi_data():
    """A function that collects a list of variable ECG csv files and expresses \
    them as a pandas DataFrame.

    :param list_: a list of all csv filenames

    :returns: data from multiple csv files expressed as a pandas DataFrame
    :raises:
    """

    import glob
    list_ = glob.glob("test_data/variable/*.csv")
    import pandas as pd
    multi_df = []
    for file in range(len(list_)):
        df = pd.read_csv(list_[i], header=None)
        multi_df.append(df)
    return multi_df

if __name__ == '__main__':
    main()
