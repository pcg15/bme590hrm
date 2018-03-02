def signal_processing(filename):
    import numpy as np
    import pandas as pd
    from extract_data import extract_template_data
    from extract_data import extract_voltage_data
    from extract_data import extract_time_data
    from import_data import import_data
    template = pd.read_csv("test_data/template.csv", header=None)
    norm_template = extract_template_data(template)
    norm_voltage = extract_voltage_data(filename)
    correlation = np.correlate(norm_template, norm_voltage, mode="full")
    return correlation
