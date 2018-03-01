def plot_data():
    import pandas as pd
    from pathlib import Path
    import matplotlib as mpl
    mpl.use('TkAgg')
    import matplotlib.pyplot as plt
#
    file_choice = input("Filename: ")
    choice = Path("test_data/"+file_choice)
    if choice.exists():
        single_df = pd.read_csv("test_data/"+file_choice, header=None)
#
    single_df.columns = ["time", "voltage"]
    single_df.plot(x="time",y="voltage")
    plt.show()

if __name__ == '__main__':
    plot_data()
