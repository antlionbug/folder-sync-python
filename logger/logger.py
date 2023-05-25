"""This file permits to set logger with time stamp."""
import logging


# should be done before to use any logging method
def initial_configuration():
    logging.basicConfig(
        format="%(asctime)s %(levelname)-8s %(message)s",
        level=logging.INFO,
        datefmt="%Y-%m-%d %H:%M:%S",
    )


def setup(name, level=logging.INFO):
    """
    To set-up as many loggers as you want
    """

    logger = logging.getLogger(name)
    logger.setLevel(level)

    return logger
