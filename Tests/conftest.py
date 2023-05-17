import os


import pytest
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

import DBConfigurations.Config_file





def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    global driver
    browserName = request.config.getoption("browser_name")
    from selenium.webdriver.chrome.options import Options
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    if browserName == "chrome":
        sevice_obj = Service(r"C:\\Selenium Softwares\\chromedriver.exe")
        driver = webdriver.Chrome(service=sevice_obj)
        driver = webdriver.Chrome(r"C:\\Selenium Softwares\\chromedriver.exe")




    driver.get(DBConfigurations.Config_file.Url)
    driver.maximize_window()
    request.cls.driver = driver
    driver.implicitly_wait(40)
    # yield
    # driver.close()



    # @pytest.fixture(scope='session')
    # def jira_cookie():
    #     url = 'https://localhost:7070/rest/auth/1/session'
    #     username = 'mohan.sonone'
    #     password = 'Shiv@4222'
    #
    #     #Make a POST request to Jira REST API to authenticate and retrieve the cookie
    #     response = requests.post(url, json={'mohan.sonone': username, 'Shiv@4222': password})
    #     cookie = response.cookies.get_dict()
    #
    #     yield cookie
# Report Name Std code
def pytest_html_report_title(report):
    report.title = "DataBase Testing HTML report!"