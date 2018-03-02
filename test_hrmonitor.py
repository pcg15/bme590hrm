import numpy as np
filename = "test_data1.csv"


def test_HRMonitor():
    from pathlib import Path
    from hrmonitor import HRMonitor
    choice = Path("test_data1.json")
    function = HRMonitor(filename)
    assert function.duration == 27.775
    assert function.voltage_extremes == (-0.68, 1.05)
    assert function.num_beats == 31
    assert function.mean_hr_bpm == 78.0
    assert choice.exists()


def test_beats():
    from beats import beats
    assert len(beats(filename)) == 31


def test_duration():
    from duration import duration
    assert duration(filename) == 27.775


def test_import_data():
    from pathlib import Path
    choice = Path("test_data/"+filename)
    assert choice.exists()


def test_json_maker():
    from pathlib import Path
    choice = Path("test_data1.json")
    assert choice.exists()


def test_mean_hr_bpm():
    from mean_hr_bpm import mean_hr_bpm
    assert mean_hr_bpm(filename) == 78.0


def test_num_beats():
    from num_beats import num_beats
    assert num_beats(filename) == 31


def test_signal_processing():
    from extract_data import extract_template_data
    from extract_data import extract_voltage_data
    from signal_processing import signal_processing
    x = extract_voltage_data(filename)
    y = extract_template_data(filename)
    correlation = np.correlate(y, x, mode="full")
    assert len(signal_processing(filename)) == len(correlation)


def test_voltage_extremes():
    from voltage_extremes import voltage_extremes
    assert voltage_extremes(filename) == (-0.68, 1.05)


def test_exceptions():
    import pytest
    import math
    with pytest.raises(ImportError, message="Anticipated ImportError"):
        import anypackage
    with pytest.raises(TypeError, message="Anticipated TypeError"):
        int_list = 1 + [1, 2, 4]
        int_str = 3 + "hello"
        list_str = [1, 2, 4] + "hello"
    with pytest.raises(ValueError, message="Anticipated ValueError"):
        val = int("hello")
