def mean_hr_bpm():
    import pandas as pd
    import numpy as np
    template = pd.read_csv("test_data/template.csv", header=None)
    fit = template.values
    fit = fit.squeeze()
    fit = fit.tolist()


if __name__ == '__main__':
    mean_hr_bpm()
