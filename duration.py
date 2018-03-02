def duration(filename):
    import pandas as pd
    from import_data import import_data
    df = import_data(filename)
    df.columns = ["time", "voltage"]
    duration = df["time"].max()
    return duration
