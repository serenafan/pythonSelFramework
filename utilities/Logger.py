"""
logger builder
"""

import logging
import sys


class Logger:
    """
    Class of logger builder
    """

    @staticmethod
    def getLogger():
        """
        Building log file and format
        """
        logger = logging.getLogger()
        logging.basicConfig(format="%(asctime)s: %(levelname)s: %(filename)s: %(message)s",
                            encoding="utf-8",
                            stream=sys.stdout,
                            level=logging.DEBUG)
        return logger


log = Logger.getLogger()