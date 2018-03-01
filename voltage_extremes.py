def voltage_extremes():
    import pandas as pd
    df = single_df
    df.columns = ["time", "voltage"]
    voltage_min = df["voltage"].min()
    voltage_max = df["voltage"].max()
    display = (voltage_min, voltage_max)

if __name__ == '__main__':
    voltage_extremes()
