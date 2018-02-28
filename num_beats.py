def num_beats(file_):

    """...

    :param:

    :returns:
    :raises ImportError:
    :raises TypeError:
    :raises ValueError:
    """

    import logging
    str_ = logging.DEBUG
    logging.basicConfig(filename="hrmonitorlog.txt", format='%(levelname)s \
    %(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=str_)
