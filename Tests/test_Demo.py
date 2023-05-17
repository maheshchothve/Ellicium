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
from PageObjects.Dropdown import All_elements
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

        allelements=All_elements(self.driver)


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


        # def dropDownSelection(driver, dropDownList, expVal, dropDownName):
        #     for i in range(1, len(dropDownList) + 1):
        #         name = driver.find_element(By.XPATH,
        #                                    "(//div[@class='slicerBody' and @aria-label='" + dropDownName + "']//div[@class='slicerItemContainer']/span)[" + str(
        #                                        i) + "]")
        #         nameSel = driver.find_element(By.XPATH,
        #                                       "(//div[@class='slicerBody' and @aria-label='" + dropDownName + "']//div[@class='slicerItemContainer']/span)[" + str(
        #                                           i) + "]/preceding-sibling::div")
        #
        #         print("Name: " + name.text)
        #         print("NameSel: " + nameSel.get_attribute("class"))
        #         if name.text == expVal:
        #             if nameSel.get_attribute("class") != "slicerCheckbox selected":
        #                 name.click()
        #                 print("Selected " + expVal)
        #                 break
        #             else:
        #                 print("Already Selected " + expVal)
        #
        # time.sleep(6)
        # time.sleep(3)
        #
        # expVal = "G P Mumbai"
        # expValCrse = "Computer Engineering"
        # expValSem = "Semester 1"
        # expValSub = "Engineering Drawing"
        # expValLect = "V V Marathe"
        # expValStud = "Aditi M"
        #
        # print("-------------------Institute Name------------------------")
        # self.driver.find_element(By.XPATH, "//div[@class='slicer-dropdown-menu' and @aria-label='Institute_name']/i").click()
        # time.sleep(5)
        # ins_nameList = self.driver.find_elements(By.XPATH, "//div[@class='slicerBody' and @aria-label='Institute_name']//div[@class='slicerItemContainer']/span")
        # dropDownSelection(self.driver, ins_nameList, expVal, "Institute_name")
        # ins_name=[]
        # for insti in  ins_nameList:
        #     ins_name.append(insti.text)
        #
        # log.info("Removing_unwanted_string")
        # unwanted_string = '(Blank)'
        # while unwanted_string in ins_name:
        #     ins_name.remove(unwanted_string)
        # print("Total institutes from dashboard are", ins_name)
        # obj=DatabaseConnection
        # database_Testing1_insti_name =obj.Query1(self.driver)
        # print("database institute names are",database_Testing1_insti_name)
        # database_institute_names = [name[0] for name in database_Testing1_insti_name]
        # # Compare the lists
        # if set(database_institute_names) == set(ins_name):
        #     print("The lists match.")
        # else:
        #     print("The lists do not match.")
        #
        # print("-------------------course Name------------------------")
        # # Course Name
        # time.sleep(3)
        # self.driver.find_element(By.XPATH, "//div[@class='slicer-dropdown-menu' and @aria-label='Course_name']/i").click()
        # time.sleep(5)
        #
        # cse_nameList = self.driver.find_elements(By.XPATH,"//div[@class='slicerBody' and @aria-label='Course_name']//div[@class='slicerItemContainer']/span")
        # dropDownSelection(self.driver, cse_nameList, expValCrse, "Course_name")
        # course_name = []
        # for course in cse_nameList:
        #     course_name.append(course.text)
        # print("dashborad course names are",course_name)
        # obj = DatabaseConnection
        # database_Testing1_course_name = obj.Query2(self.driver)
        # print("database institute names are", database_Testing1_course_name)
        #
        #
        # print("-------------------semester ------------------------")
        # # Semester
        # time.sleep(3)
        # self.driver.find_element(By.XPATH, "//div[@class='slicer-dropdown-menu' and @aria-label='semester']/i").click()
        # time.sleep(5)
        #
        # sem_nameList = self.driver.find_elements(By.XPATH,"(//div[@class='slicerBody' and @aria-label='semester']//div[@class='slicerItemContainer']/span)")
        # dropDownSelection(self.driver, sem_nameList, expValSem, "semester")
        # semester_name = []
        # for sem in sem_nameList:
        #     semester_name.append(sem.text)
        # print("dashborad semester names are", semester_name)
        #
        #
        # # Subject Name from Semester 1 of Computer Engineering
        # print("-------------------subject ------------------------")
        # time.sleep(3)
        # self.driver.find_element(By.XPATH, "//div[@class='slicer-dropdown-menu' and @aria-label='Subject_name']/i").click()
        # time.sleep(5)
        #
        # sub_nameList = self.driver.find_elements(By.XPATH,"(//div[@class='slicerBody' and @aria-label='Subject_name']//div[@class='slicerItemContainer']/span)")
        # dropDownSelection(self.driver, sub_nameList, expValSub, "Subject_name")
        # subject_name = []
        # for subject in sub_nameList:
        #     subject_name.append(subject.text)
        # print("dashborad subject names are", subject_name)
        #
        #
        # print("-------------------Lecturer ------------------------")
        # # Lecturer Selection
        # time.sleep(3)
        # self.driver.find_element(By.XPATH, "//div[@class='slicer-dropdown-menu' and @aria-label='Teacher Name']/i").click()
        # time.sleep(5)
        # lect_nameList = self.driver.find_elements(By.XPATH,"(//div[@class='slicerBody' and @aria-label='Teacher Name']//div[@class='slicerItemContainer']/span)")
        # dropDownSelection(self.driver, lect_nameList, expValLect, "Teacher Name")
        # lecturer_name = []
        # for lect in lect_nameList:
        #     lecturer_name.append(lect.text)
        # print("dashborad lecturer names are", lecturer_name)


        # print("-------------------Student Names------------------------")
        # # StudentName
        # time.sleep(3)
        # self.driver.find_element(By.XPATH, "//div[@class='slicer-dropdown-menu' and @aria-label='Student_name']/i").click()
        # time.sleep(5)
        #
        # stud_nameList = self.driver.find_elements(By.XPATH,"(//div[@class='slicerBody' and @aria-label='Student_name']//div[@class='slicerItemContainer']/span)")
        # dropDownSelection(self.driver, stud_nameList, expValStud, "Student_name")
        # stud_name = []
        # for student in stud_nameList:
        #     stud_name.append(student.text)
        # print("dashborad students names are", stud_name)

        # def dropDownSelection(driver, dropDownList, expVal, dropDownName):
        #     for i in range(1, len(dropDownList) + 1):
        #         name = driver.find_element(By.XPATH,
        #                                    "(//div[@class='slicerBody' and @aria-label='" + dropDownName + "']//div[@class='slicerItemContainer']/span)[" + str(i) + "]")
        #         nameSel = driver.find_element(By.XPATH,
        #                                       "(//div[@class='slicerBody' and @aria-label='" + dropDownName + "']//div[@class='slicerItemContainer']/span)[" + str(i) + "]/preceding-sibling::div")
        #
        #         print("Name: " + name.text)
        #         print("NameSel: " + nameSel.get_attribute("class"))
        #         if name.text == expVal:
        #             if nameSel.get_attribute("class") != "slicerCheckbox selected":
        #                 name.click()
        #                 print("Selected " + expVal)
        #                 break
        #             else:
        #                 print("Already Selected " + expVal)
        #
        # def get_dropdown_values(driver, dropdown_name, expected_value):
        #     time.sleep(3)
        #     dropdown_xpath = "//div[@class='slicer-dropdown-menu' and @aria-label='" + dropdown_name + "']/i"
        #     driver.find_element(By.XPATH, dropdown_xpath).click()
        #     time.sleep(5)
        #
        #     dropdown_list = driver.find_elements(By.XPATH,
        #                                          "//div[@class='slicerBody' and @aria-label='" + dropdown_name + "']//div[@class='slicerItemContainer']/span")
        #     dropDownSelection(driver, dropdown_list, expected_value, dropdown_name)
        #
        #     dropdown_values = []
        #     for item in dropdown_list:
        #         dropdown_values.append(item.text)
        #     print("Dashboard", dropdown_name, "names are", dropdown_values)
        #     return dropdown_values
        #
        # time.sleep(6)
        # time.sleep(3)
        #
        # expVal = "G P Mumbai"
        # expValCrse = "Computer Engineering"
        # expValSem = "Semester 1"
        # expValSub = "Engineering Drawing"
        # expValLect = "V V Marathe"
        # expValStud = "Aditi M"
        #
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
        # print("database institute names are",database_Testing1_insti_name)
        # database_institute_names = [name[0] for name in database_Testing1_insti_name]
        # # # Compare the lists
        # if set(database_institute_names) == set(ins_name):
        #     print("The lists match.")
        # else:
        #     print("The lists do not match.")
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
        # #
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
        # #
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

        # marksobtained_xpath = "//*[@id='pvExplorationHost']/div/div/exploration/div/explore-canvas/div/div[2]/div/div[2]/div[2]/visual-container-repeat/visual-container[22]/transform/div/div[2]/div/visual-modern/div/svg/g[1]/text/tspan"
        # print("marks obtaied are",self.driver.find_element(By.XPATH, marksobtained_xpath).get_text())

        # Execute JavaScript to unhide the element
        element = self.driver.find_element(By.XPATH,"//*[@id='pvExplorationHost']/div/div/exploration/div/explore-canvas/div/div[2]/div/div[2]/div[2]/visual-container-repeat/visual-container[22]/transform/div/div[2]/div/visual-modern/div/svg")

        self.driver.execute_script("arguments[0].style.overflow = 'visible';", element)
        element1="//*[@id='pvExplorationHost']/div/div/exploration/div/explore-canvas/div/div[2]/div/div[2]/div[2]/visual-container-repeat/visual-container[22]/transform/div/div[2]/div/visual-modern/div/svg/g[1]/text/tspan"
        print("marks obtaied are", self.driver.find_element(By.XPATH, element1).text)













































