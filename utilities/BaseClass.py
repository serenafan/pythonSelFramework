import inspect
import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class BaseClass:
    def waitLinkPresence(self, text):
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, text)))

    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)

        # file handler object
        fileHandler = logging.FileHandler("logfile.log")

        # log format
        formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)

        # LEVEL: debug, info, warning, error, critical
        logger.setLevel(logging.INFO)
        return logger
