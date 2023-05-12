import time

import pytest
import softest
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

import DBConfigurations.Config_file


from PageObjects.Home_Page import HomePage
from PageObjects.LoginPage import LoginPage
from Utility.BaseClass import BaseClass2
from Utility.DatabaseUtility import DatabaseConnection


class Test_database(BaseClass2, softest.TestCase):
    Excel_report = DBConfigurations.Config_file.Excel_Report_File
    Excel_sheet_name = DBConfigurations.Config_file.Sheet_Name

    def test_PowerBI(self):
        log = self.getLogger()

        loginpage = LoginPage(self.driver)
        self.driver.implicitly_wait(30)

        homepage = HomePage(self.driver)
        self.driver.implicitly_wait(30)

        #DBdata = self.dbconncetions()

        self.driver.implicitly_wait(30)
        log.info("Entering Email")
        loginpage.Enter_mail().send_keys(DBConfigurations.Config_file.PowerBi_UserName)

        self.driver.implicitly_wait(30)
        log.info("clicking on submit")
        loginpage.Enter_submit().click()

        time.sleep(5)
        self.driver.implicitly_wait(30)
        log.info("Entering Password")
        loginpage.password().send_keys(DBConfigurations.Config_file.PowerBi_Password)

        self.driver.implicitly_wait(30)
        log.info("clicking on Signin Button")
        loginpage.MS_SigninConfButton().click()

        self.driver.implicitly_wait(30)
        log.info("clicking on stay Signin Button")
        time.sleep(10)
        if loginpage.staysigninpage().is_displayed():
            loginpage.staysigninpage().click()

        # #checking for the image is displayed or not
        # image=homepage.imageBag1().is_displayed()
        # print("image is diplayed",image)

        # #assertion for the page title
        # print(homepage.Title().text)
        # assert homepage.Title().text == "Student's Performance "
        #
        #
        # log.info("click on the dropdownn button for Institute")
        homepage.Institue().click()
        #
        # log.info("checking for the slicer for institue")
        # slicer_item = homepage.slicier1()
        #
        # # Find the checkbox element within the slicer item
        # checkbox = slicer_item.find_element(By.XPATH, ".//span[contains(@class, 'checkboxOutlineContrast')]")
        #
        # # Check if the checkbox is selected
        # if not checkbox.get_attribute("class").endswith("selected"):
        #     checkbox.click()
        #
        # # selecting COURSE  dropdown button
        # homepage.CourseDropdown1().click()
        #
        # # Selecting 'computer engineering'.
        # slicer_course=homepage.slicier2()
        #
        # checkbox1=slicer_course.find_element(By.XPATH,".//span[contains(@class, 'checkboxOutlineContrast')]")
        #
        # if not checkbox1.get_attribute("class").endswith("selected"):
        #     checkbox1.click()
        #
        # #SELCTING THE SEM DROPDOWN
        # homepage.Semdropdown().click()
        # # selecting the slicier for SEMESTER1
        # slicier_sem=homepage.slicier3()
        # checkbox2 = slicier_sem.find_element(By.XPATH, ".//span[contains(@class, 'checkboxOutlineContrast')]")
        #
        # if not checkbox2.get_attribute("class").endswith("selected"):
        #     checkbox2.click()

        #SELECTING SUBJECT DROPDOWN
        # homepage.Subjectdropdown().click()
        # #slecting slicier for subject ED
        # slicer_subject=homepage.slicier4()
        # checkbox3=slicer_subject.find_elements(By.XPATH,".//span[contains(@class, 'checkboxOutlineContrast')]")
        # if not checkbox3.get_attribute("class").endswith("selected"):
        #     checkbox3.click()
        obj = DatabaseConnection()
        database_Testing4_tuple_list = obj.Query1()

        print("database course name",database_Testing4_tuple_list)

        database_Institute_name=obj.Query2()
        print("database institue name is ",database_Institute_name)

        instute_name=homepage.InstituteName1().text
        print("name of college is",instute_name)













