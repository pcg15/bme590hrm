def voltage_extremes(filename):
    import pandas as pd
    from import_data import import_data
    df = import_data(filename)
    df.columns = ["time", "voltage"]
    voltage_min = df["voltage"].min()
    voltage_max = df["voltage"].max()
    voltage_extremes = (voltage_min, voltage_max)
    return voltage_extremes
