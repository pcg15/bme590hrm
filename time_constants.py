def time_endpoint(filename):
    from extract_data import extract_time_data
    total_time = extract_time_data(filename) #time vector from signal
    end_time = np.max(total_time) #the last time point of signal
    return end_time

def time
