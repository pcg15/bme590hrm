def mean_hr_bpm():
    import pandas as pd
    import numpy as np
    template = pd.read_csv("test_data/template.csv", header=None)
#
    from pathlib import Path
    file_choice = input("Filename: ")
    choice = Path("test_data/"+file_choice)
    print(choice)
    if choice.exists():
        single_df = pd.read_csv("test_data/"+file_choice, header=None)
#
    df = single_df
    df = np.ravel(df)
    corr = np.correlate(template,single_df, mode="full")
    print(corr)

if __name__ == '__main__':
    mean_hr_bpm()
