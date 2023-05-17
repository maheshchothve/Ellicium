import time

import pytest
import softest
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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



        def dropDownSelection(driver, dropDownList, expVal, dropDownName):
            for i in range(1, len(dropDownList) + 1):
                name = driver.find_element(By.XPATH,
                                           "(//div[@class='slicerBody' and @aria-label='" + dropDownName + "']//div[@class='slicerItemContainer']/span)[" + str(i) + "]")
                nameSel = driver.find_element(By.XPATH,
                                              "(//div[@class='slicerBody' and @aria-label='" + dropDownName + "']//div[@class='slicerItemContainer']/span)[" + str(i) + "]/preceding-sibling::div")

                print("Name: " + name.text)
                print("NameSel: " + nameSel.get_attribute("class"))
                if name.text == expVal:
                    if nameSel.get_attribute("class") != "slicerCheckbox selected":
                        name.click()
                        print("Selected " + expVal)
                        break
                    else:
                        print("Already Selected " + expVal)

        def get_dropdown_values(driver, dropdown_name, expected_value):
            time.sleep(3)
            dropdown_xpath = "//div[@class='slicer-dropdown-menu' and @aria-label='" + dropdown_name + "']/i"
            driver.find_element(By.XPATH, dropdown_xpath).click()
            time.sleep(5)

            dropdown_list = driver.find_elements(By.XPATH,
                                                 "//div[@class='slicerBody' and @aria-label='" + dropdown_name + "']//div[@class='slicerItemContainer']/span")
            dropDownSelection(driver, dropdown_list, expected_value, dropdown_name)

            dropdown_values = []
            for item in dropdown_list:
                dropdown_values.append(item.text)
            print("Dashboard", dropdown_name, "names are", dropdown_values)
            return dropdown_values

        def compare_dashboard_database(driver,dropdown_name,dashboard_values,database_query):
            print(f"{dropdown_name} from dashboard are{dashboard_values}")
            obj = DatabaseConnection
            database_values = obj.Query(driver, database_query)
            print(f"{dropdown_name} from database values are{database_values}")
            database_values = [name[0] for name in database_values]
        # Compare the lists
            if set(database_values) == set(dashboard_values):
                 print("The lists match.")
            else:
                print("The lists do not match.")

        time.sleep(6)
        time.sleep(3)

        expVal = "G P Mumbai"
        expValCrse = "Computer Engineering"
        expValSem = "Semester 1"
        expValSub = "Engineering Drawing"
        expValLect = "V V Marathe"
        expValStud = "Aditi M"
        ins_name = get_dropdown_values(self.driver, "Institute_name", expVal)
        compare_dashboard_database(self.driver, "Institute Name", ins_name, 2)

        course_name = get_dropdown_values(self.driver, "Course_name", expValCrse)
        compare_dashboard_database(self.driver, "Course Name", course_name, 3)

        semester_name = get_dropdown_values(self.driver, "semester", expValSem)
        # compare_dashboard_database(self.driver, "Semester", semester_name, )

        subject_name = get_dropdown_values(self.driver, "Subject_name", expValSub)
        compare_dashboard_database(self.driver, "Subject", subject_name, 5)

        lecturer_name = get_dropdown_values(self.driver, "Teacher Name", expValLect)
        compare_dashboard_database(self.driver, "lecturer", lecturer_name, 6)

        stud_name = get_dropdown_values(self.driver, "Student_name", expValStud)
        compare_dashboard_database(self.driver, "Student name", stud_name, 7)

        # print("-------------------Institute Name------------------------")
        # ins_name = get_dropdown_values(self.driver, "Institute_name", expVal)
        #
        # log.info("Removing_unwanted_string")
        # unwanted_string = '(Blank)'
        # while unwanted_string in ins_name:
        #     ins_name.remove(unwanted_string)
        # print("Total institutes from dashboard are", ins_name)
        # obj = DatabaseConnection
        # database_Testing1_insti_name =obj.Query(self.driver,2)
        #
        #
        # # # Rest of the code using the function for other dropdowns
        #
        # print("-------------------course Name------------------------")
        # course_name = get_dropdown_values(self.driver, "Course_name", expValCrse)
        # database_Testing_course_name = obj.Query(self.driver,3)
        # print("database course names are", database_Testing_course_name)
        # database_Testing_course_name = [name[0] for name in database_Testing_course_name]
        # # Compare the lists
        # if set(database_Testing_course_name) == set(course_name):
        #     print("The lists match.")
        # else:
        #     print("The lists do not match.")
        #
        #
        # print("-------------------semester ------------------------")
        # semester_name = get_dropdown_values(self.driver, "semester", expValSem)
        # #
        # print("-------------------subject ------------------------")
        # subject_name = get_dropdown_values(self.driver, "Subject_name", expValSub)
        # database_Testing_subject_name = obj.Query(self.driver, 5)
        # print("database subject names are", database_Testing_subject_name)
        # database_Testing_subject_name = [name[0] for name in database_Testing_subject_name]
        # # Compare the lists
        # if set(database_Testing_subject_name) == set(subject_name):
        #     print("The lists match.")
        # else:
        #     print("The lists do not match.")
        #
        #
        # print("-------------------Lecturer ------------------------")
        # lecturer_name = get_dropdown_values(self.driver, "Teacher Name", expValLect)
        # database_Testing_lecturer_name = obj.Query(self.driver, 6)
        # print("database subject names are", database_Testing_lecturer_name)
        # database_Testing_lecturer_name = [name[0] for name in database_Testing_lecturer_name]
        # # Compare the lists
        # if set(database_Testing_lecturer_name) == set(lecturer_name):
        #     print("The lists match.")
        # else:
        #     print("The lists do not match.")
        #
        #
        # print("-------------------Student Names------------------------")
        # stud_name = get_dropdown_values(self.driver, "Student_name", expValStud)
        # database_Testing_student_name = obj.Query(self.driver, 7)
        # print("database subject names are", database_Testing_student_name)
        # database_Testing_student_name = [name[0] for name in database_Testing_student_name]
        # # Compare the lists
        # if set(database_Testing_student_name) == set(stud_name):
        #     print("The lists match.")
        # else:
        #     print("The lists do not match.")
















































