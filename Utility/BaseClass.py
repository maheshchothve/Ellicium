import inspect
import logging
import socket
import sys

import openpyxl
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
import pyodbc
from selenium.webdriver.support import expected_conditions as EC

import DBConfigurations


@pytest.mark.usefixtures("setup")
class BaseClass2:

    def getLogger(self):
        loggerName = inspect.stack()[1][3]

        logger = logging.getLogger(loggerName)

        fileHandler = logging.FileHandler("logfile.log")

        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s : %(message)s ")

        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)
        hostname=socket.gethostname()
        logger.setLevel(logging.NOTSET)
        console= logging.StreamHandler(sys.stdout)
        console.setFormatter(formatter)
        logging.getLogger().addHandler(console)
        log=logging.getLogger(hostname)

        return logger

    def wait_for_element_by_xpath(self):
        wait = WebDriverWait(self.driver, 10)

        return wait


# def take_screenshot(self, test_name):
#     screenshots_dir = DBConfigurations.Config.screenshots_dir
#     screenshot_file_path = DBConfigurations.Config.screenshots_dir.format(screenshots_dir, test_name)
#     self.save_screenshot(screenshot_file_path)

