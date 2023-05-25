"""This file permits to set logger with time stamp."""
import logging
import datetime
import os
import sys


# should be done before to use any logging method
def initial_configuration(path):
    logging.basicConfig(
        filename=path,
        encoding='utf-8',
        format="%(asctime)s %(levelname)-8s %(message)s",
        level=logging.INFO,
        datefmt="%Y-%m-%d %H:%M:%S",
    )


def setup(name, level=logging.INFO):
    """
    To set-up as many loggers as you want
    """
    logging.getLogger().addHandler(logging.StreamHandler())
    logger = logging.getLogger(name)
    logger.setLevel(level)

    return logger


def generate_name(path):
    filename = path + str(datetime.date.today()) + "_Logs"

    i = 1
    filename_temp = filename
    while True:
        if not os.path.isfile(filename_temp):
            filename = filename_temp
            break
        else:
            filename_temp = filename + f"_{i}"
            i += 1

    return filename
