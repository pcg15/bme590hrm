def json_maker():
    import json
    filechoice = filechoice[:-4]
    data = {
        "Average Heart Rate" : str(df.mean_hr_bpm) + " bpm",
        "Minimum and Maximum Lead Voltages" : str(df.voltage_extremes) + " mV",
        "Duration of Signal" : str(df.duration) + " seconds",
        "Number of Beats Detected" : str(df.num_beats) + " beats",
        "Times When a Beat Occured" : str(df.beats)
    }
    with open(str(filechoice)+".json", 'w') as f:
        json.dump(data, f)

if __name__ == '__main__':
    json_maker()
