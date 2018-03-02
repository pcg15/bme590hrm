filename = "test_data1.csv"

def test_HRMonitor(filename):
    from pathlib import Path
    from hrmonitor import HRMonitor
    choice = Path("test_data1.json")
    function = HRMonitor(filename)
    assert function.duration == 27.775
    assert function.voltage_extremes == (-0.68, 1.05)
    assert function.num_beats == 31
    assert len(function.beats) == 31
##############
    assert function.mean_hr_bpm == 78.0
    assert choice.exists()

def test_beats(filename):
    from beats import beats
    assert beats(filename) == 31

def test_duration(filename):
    from duration import duration
    assert duration(filename) == 27.775

def test_extract_data(filename):
    from extract_data import extract_voltage_data
    from extract_data import extract_time_data
    from extract_data import extract_template_data
    assert np.max(extract_time_data(filename)) == 27.775
    assert np.max()


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
