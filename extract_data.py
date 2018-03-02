def extract_voltage_data(filename):
    import numpy as np
    from import_data import import_data
    df = import_data(filename)
    values = df.values
    voltage = values[:,1]
    norm_voltage = voltage - np.mean(voltage)
    return norm_voltage

def extract_time_data(filename):
    from import_data import import_data
    df = import_data(filename)
    values = df.values
    time = values[:,0]
    return time

def extract_template_data(template):
    import numpy as np
    temp_values = template.values
    temp_vol = temp_values[:,1]
    norm_template = temp_vol - np.mean(temp_vol)
    return norm_template
