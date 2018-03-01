def duration():
    import pandas as pd
    df = single_df
    df.columns = ["time", "voltage"]
    duration = df["time"].max()
    display = str(duration) + " seconds"
    print(display)

if __name__ == '__main__':
    duration()
