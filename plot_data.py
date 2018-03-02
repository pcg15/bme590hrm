def plot_data(filename):
    """module to visualize ECG data and calculations

    :param filename: the name of a file located in the /test_data folder \
    entered as a string

    :returns plot: matplotlib plot of data
    """
    import pandas as pd
    from pathlib import Path
    import matplotlib as mpl
    mpl.use('TkAgg')
    import matplotlib.pyplot as plt
    choice = Path("test_data/"+filename)
    if choice.exists():
        single_df = pd.read_csv("test_data/"+file_choice, header=None)
    single_df.columns = ["time", "voltage"]
    single_df.plot(x="time",y="voltage")
    plt.show()
