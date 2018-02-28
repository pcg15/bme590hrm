import logging
str_ = logging.DEBUG
logging.basicConfig(filename="hrmonitorlog.txt", format='%(levelname)s \
%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=str_)


class HRMonitor:

    """Program...

    :param:

    :returns:

    :raises ImportError:
    :raises TypeError:
    :raises ValueError:
    """

    def __init__(self, file_=):
        self.file_ = file_
        self.Sum = None
        self.FindSummation()
        self.MinMax = None
        self.FindMinMax()
        self.MaxDiff = None
        self.FindMaxDifference()
