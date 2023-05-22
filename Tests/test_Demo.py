import time

import pytest
import softest
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote import switch_to
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


import DBConfigurations.Config_file
import Tests

from PageObjects.Home_Page import HomePage
from PageObjects.LoginPage import LoginPage
from Tests.conftest import setup

from Utility.BaseClass import BaseClass2
from Utility.DatabaseUtility import DatabaseConnection



class Test_database(BaseClass2):
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
            # print("Dashboard", dropdown_name, "names are", dropdown_values)
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

        print("---------------------comparing the data from dropdownss-----------------------------")
        ins_name = get_dropdown_values(self.driver, "Institute_name", expVal)
        unwanted_string = '(Blank)'
        while unwanted_string in ins_name:
            ins_name.remove(unwanted_string)
        print("Total institutes from dashboard are", ins_name)
        compare_dashboard_database(self.driver, "Institute Name", ins_name, 2)

        log.info("comparing the course name from database and dashboard")
        course_name = get_dropdown_values(self.driver, "Course_name", expValCrse)
        compare_dashboard_database(self.driver, "Course Name", course_name, 3)

        log.info("comparing the semester from database and dashboard")
        semester_name = get_dropdown_values(self.driver, "semester", expValSem)
        # compare_dashboard_database(self.driver, "Semester", semester_name, )
        #
        subject_name = get_dropdown_values(self.driver, "Subject_name", expValSub)
        compare_dashboard_database(self.driver, "Subject", subject_name, 5)
        #
        lecturer_name = get_dropdown_values(self.driver, "Teacher Name", expValLect)
        compare_dashboard_database(self.driver, "lecturer", lecturer_name, 6)
        #
        stud_name = get_dropdown_values(self.driver, "Student_name", expValStud)
        compare_dashboard_database(self.driver, "Student name", stud_name, 7)




        print("---------------------months and  attendence  vertical tables ------------------------------------------------")
        months_list=self.driver.find_elements(By.CSS_SELECTOR,"svg[name$='Line and stacked column chart'] text[class ='setFocusRing']")
        monthlist=[]
        for month in months_list:
            monthlist.append(month.text)

        # print(monthlist)

        attendece=self.driver.find_elements(By.CSS_SELECTOR,"svg[name$='Line and stacked column chart'] g[class=series] rect")
        attendece_list=[]

        for atten in attendece:
            # [2:6]
            per=atten.get_attribute("aria-label")[2:6]
            attendece_list.append(float(per)/100.00)

        print(attendece_list)

        month_attendence = {}
        # COnvert to dictionary
        for key in monthlist:
            for value in attendece_list:
                month_attendence[key] = value
                attendece_list.remove(value)
                break
        print("monthwise attendence for the student is :\n ", month_attendence)

        month_attendence_database=[]
        for i in  range(30,35):
            obj = DatabaseConnection
            value = obj.Query(self.driver,i)
            month_attendence_database.append(value)

        print(month_attendence_database)

        for entry in month_attendence_database:
            month, percentage = entry[0]
            if month in month_attendence:
                dashboard_percentage = month_attendence[month]
                if percentage == dashboard_percentage:
                    print(f"Data for {month} matches: {percentage}")
                else:
                    print(
                        f"Data for {month} does not match: Dashboard - {dashboard_percentage}, Database - {percentage}")
            else:
                print(f"Data for {month} not found in the dashboard")



        print("----------------------------------------------comparing the total marks  second row of marks from UI---------------------------------")
        #
        def database_secondrow(value,row):
            obj = DatabaseConnection
            value = obj.Query(self.driver,row)
            marksofaditi = []
            marksofaditi.extend(value)
            return marksofaditi

        marksofaditi=database_secondrow("marks_obtained",9)
        marksofaditi.extend(database_secondrow("total_marks", 14))
        marksofaditi.extend(database_secondrow("percentage_marks_aditi", 15))
        marksofaditi.extend(database_secondrow("Percentage attendece of aditi", 20))
        print(marksofaditi)
        marksofaditi = [name[0] for name in marksofaditi]
        print("MARKS_OBTAINED,TOTAL MARKS,MARKS PERCENTAGE,ATTENDENCE PERCENTAGE FROM DATABASE ARE",marksofaditi)

        tSmryList = self.driver.find_elements(By.CSS_SELECTOR,
                                         "div.visual.visual-card.customPadding.allow-deferred-rendering svg tspan")

        mrk = []
        i = 0
        marks = ""
        groupNum = ""
        groupName = ""

        for ele in tSmryList:
            if i == 2:
                groupNum = ele.text
                print("GroupNo:", groupNum)

            if i == 3:
                groupName = ele.text
                print("GroupName:", groupName)

            if 4 <= i < len(tSmryList):
                # print("AllMarksSmmry:", ele.text, "- Index:", tSmryList.index(ele))
                marks = ele.text

                if 4 <= i <= 5:
                    mrk.append(int(marks))

                if 6 <= i < len(tSmryList):
                    if "%" in ele.text:
                        marks = marks.replace("%", "")

                        if i == 6:
                            mrk.append(int(marks[:marks.index(".")]))
                        else:
                            print("Replace String:", marks)
                            mrk.append(float(marks))

            i += 1
        marks_from_dashboard=mrk
        print("MARKS_OBTAINED,TOTAL MARKS,MARKS PERCENTAGE,ATTENDENCE PERCENTAGE FROM DASHBOARD ARE", marks_from_dashboard)

        if set(marksofaditi) == set(marks_from_dashboard):
            print("MARKS_OBTAINED,TOTAL MARKS,MARKS PERCENTAGE,ATTENDENCE PERCENTAGE FROM DASHBOARD AND DATABSE ARE MATCHING")
        else:
            print("MARKS_OBTAINED,TOTAL MARKS,MARKS PERCENTAGE,ATTENDENCE PERCENTAGE FROM DASHBOARD AND DATABSE ARE NOT MATCHING")

        time.sleep(3)
        print("group number from dashborad is:",groupNum)
        print("group name from dashborad is",groupName)
        obj=DatabaseConnection
        groupName_database=obj.Query(self.driver,25)
        print("group name from database is",groupName_database)

        dashboard_group_number = 'I'
        database_group_name = [('I',)]

        if database_group_name:
            database_group_number = database_group_name[0][0]

            if dashboard_group_number == database_group_number:
                print(
                    f"Group number from the dashboard '{dashboard_group_number}' matches the group name from the database '{database_group_number}'.")
            else:
                print(
                    f"Group number from the dashboard '{dashboard_group_number}' does not match the group name from the database '{database_group_number}'.")
        else:
            print("No group name found in the database.")

        print("---------------------------------comparing remarks data------------------")
        self.driver.switch_to.frame(self.driver.find_element(By.CSS_SELECTOR, "iframe[class=visual-sandbox]"))

        charList = self.driver.find_elements(By.CSS_SELECTOR, "div[id=sandbox-host] g[class=word] text:nth-of-type(1)")
        # print("Size of List:", len(charList))

        charListCmp = []
        for ele in charList:
            # print("Chr:", ele.text)
            charListCmp.append(ele.text)

        print("Charactristics Summery:", charListCmp)

        self.driver.switch_to.default_content()
        obj = DatabaseConnection
        database_remarks = obj.Query(self.driver, 35)
        print("databse student performaing grid is", database_remarks)

        #
        # dashboard_characteristics_set = set(charListCmp)
        # database_characteristics_set = set(database_remarks[0][0].split(','))
        #
        # cleaned_database_characteristics = {char.strip('"') for char in database_remarks}


        print("---------------------comparing the last grid data ---------------------------------")
        gridList = self.driver.find_elements(By.CSS_SELECTOR, "div[role=columnheader]")
        gridContentList = []
        gridHeadingList = []

        for j in range(2, len(gridList) + 1):
            gridEleHeading = self.driver.find_element(By.CSS_SELECTOR, "div[role=columnheader]:nth-of-type(" + str(j) + ")")
            gridHeadingList.append(gridEleHeading.text)

            if j == 4:
                gridEleContent = self.driver.find_element(By.CSS_SELECTOR,
                                                     "div[role=gridcell]:nth-of-type(" + str(j) + ") :nth-child(1)")
                gridContentList.append(gridEleContent.text)

            else:
                gridEleContent = self.driver.find_element(By.CSS_SELECTOR, "div[role=gridcell]:nth-of-type(" + str(j) + ")")
                gridContentList.append(gridEleContent.text)

        print("GridHeading:", gridHeadingList)
        print("GridContent: from dashborad", gridContentList)

        obj=DatabaseConnection
        database_student_performing_grid=obj.Query(self.driver,36)
        print("database data for how student performing grid ",database_student_performing_grid)
        time.sleep(5)
        name_match = gridContentList[0] == database_student_performing_grid[0][0]
        subject_match = gridContentList[1] == database_student_performing_grid[0][1]
        score_match = int(gridContentList[2]) == database_student_performing_grid[0][2]
        total_score = int(gridContentList[3]) == database_student_performing_grid[0][3]
        percentage_match = float(gridContentList[4].strip('%')) == database_student_performing_grid[0][4]
        traits_match = (gridContentList[5]) == database_student_performing_grid[0][5]
        id_match = int(gridContentList[6]) == database_student_performing_grid[0][6]
        log.info("comparing the database values and dashboard values of grid at end of UI")
        if name_match and subject_match and score_match and total_score and percentage_match and id_match:
            print("The data from the dashboard and database match.")
        else:
            print("The data from the dashboard and database do not match.")



        print("-----------------------------attendence reason--------------------------")
        absentReasonList = self.driver.find_elements(By.CSS_SELECTOR,
                                                "svg[name='Stacked bar chart'] text[class='setFocusRing']")
        absentListData = []

        absentPerList = self.driver.find_elements(By.CSS_SELECTOR, "svg[name='Stacked bar chart'] text[class='label']")
        absentPerData = []

        for ele in absentReasonList:
            print("Absent Reason:", ele.text)
            absentListData.append(ele.text)

        for ele in absentPerList:
            print("Absent Per:", ele.text)
            absentPerData.append(ele.text)

        print("Absent List Reasons:", absentListData)
        print("Absent List Per:", absentPerData)
        obj = DatabaseConnection
        database_remarks = obj.Query(self.driver, 37)
        print("databse absent reason table data", database_remarks)




































































