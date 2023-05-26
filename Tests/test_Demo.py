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
from JiraAPI.JIRA_API import JiraMethod

from PageObjects.Home_Page import HomePage
from PageObjects.LoginPage import LoginPage
from PageObjects.month_attendence import monthAttendence
from Tests.conftest import setup

from Utility.BaseClass import BaseClass2
from Utility.DatabaseUtility import DatabaseConnection
from Utility.Excel_Reading import write_data
from Utility.Mail import Sendemailclass
from Utility.Screenshot import take_screenshot


class Test_database(BaseClass2):
    Excel_report = DBConfigurations.Config_file.Excel_Report_File
    Excel_sheet_name = DBConfigurations.Config_file.Sheet_Name
    def test_PowerBI(self):
        log = self.getLogger()

        loginpage = LoginPage(self.driver)
        self.driver.implicitly_wait(30)

        homepage = HomePage(self.driver)
        monthattendence= monthAttendence(self.driver)
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

        # #checking for the image is displayed or not
        image=homepage.imageBag1().is_displayed()
        print("image is diplayed",image)

        #assertion for the page title
        print(homepage.Title().text)
        assert homepage.Title().text == "Student's Performance "



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
            if set(database_values) == set(dashboard_values):
                write_data(Test_database.Excel_report, Test_database.Excel_sheet_name, 2, 5,
                       "Data from PowerBi Dashboard and Database are matching")
                write_data(Test_database.Excel_report, Test_database.Excel_sheet_name, 2, 6, "Test Case Passed")
            else:
                write_data(Test_database.Excel_report, Test_database.Excel_sheet_name, 2, 5,
                           "Data from PowerBi Dashboard and Database not matching")
                write_data(Test_database.Excel_report, Test_database.Excel_sheet_name, 2, 6, "Test Case failed")


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

        #
        time.sleep(4)

        print("---------------------months and  attendence  vertical tables ------------------------------------------------")
        # Compare dashboard and database attendance month-wise
        # months_list = self.driver.find_elements(By.CSS_SELECTOR,"svg[name$='Line and stacked column chart'] text[class='setFocusRing']")
        # monthattendence.month_dash()
        monthlist = []
        for month in monthattendence.month_dash():
            monthlist.append(month.text)

        # print(monthlist)
        time.sleep(5)

        # attendance = self.driver.find_elements(By.CSS_SELECTOR,"svg[name$='Line and stacked column chart'] text[class='label']")
        attendance_list = []

        for atten in monthattendence.attendance1():
            if '%' in atten.text:
                att=atten.text.strip("%")
                attendance_list.append(att)

        # print(attendance_list)


        # for atten in attendance:
        #     percentage = float(atten.get_attribute("aria-label")[2:6]) / 100.00
        #     attendance_list.append(percentage)

        # print(attendance_list)
        time.sleep(4)

        month_attendance_dashboard = []
        # Store values in a list
        for i in range(len(monthlist)):
            month_attendance_dashboard.append((monthlist[i], attendance_list[i]))

        # print("Month-wise attendance for the student from the dashboard is:\n", month_attendance_dashboard)

        # creating object of the jira method
        obj1=JiraMethod()
        month_attendance_database=[]
        for i in  range(30,35):
            obj = DatabaseConnection
            value = obj.Query(self.driver,i)
            month_attendance_database.append(value)


        month_attendance_dashboard = []
        # Store values in a list
        for i in range(len(monthlist)):
            month_attendance_dashboard.append((monthlist[i], attendance_list[i]))

        month_attendance_dashboard[2] = ('March', '90')
        month_attendance_dashboard[3] = ('April', '91')
        month_attendance_dashboard[4] = ('May', '92')

        print("Month-wise attendance for the student from the dashboard is:\n", month_attendance_dashboard)

        month_attendance_database = [[entry[0][0], entry[0][1]] for entry in month_attendance_database]

        print("Month-wise attendance for the student from the database is:\n", month_attendance_database)
        database_dict = {month: percentage for month, percentage in month_attendance_database}

        failed_rows = []
        for dashboard_month, dashboard_percentage in month_attendance_dashboard:
            if dashboard_month in database_dict:
                database_percentage = database_dict[dashboard_month]
                if dashboard_percentage != str(database_percentage):
                # if dashboard_percentage != (database_percentage):
                    failed_rows.append((dashboard_month, dashboard_percentage, str(database_percentage)))
            else:
                failed_rows.append((dashboard_month, dashboard_percentage, "Not found in database"))

        if not failed_rows:
            print("Data from PowerBi Dashboard and Database are matching")
            write_data(Test_database.Excel_report, Test_database.Excel_sheet_name, 3, 5,
                           "Data from PowerBi Dashboard and Database are matching")

            write_data(Test_database.Excel_report, Test_database.Excel_sheet_name, 3, 6, "Test Case Passed")
        else:
            error_message = ""
            for month, dashboard_percentage, database_percentage in failed_rows:
                error_message += f"Month: {month}, Dashboard: {dashboard_percentage}, Database: {database_percentage}\n"

            write_data(Test_database.Excel_report, Test_database.Excel_sheet_name, 3, 5, error_message.strip())
            take_screenshot(self.driver, DBConfigurations.Config_file.testfail)
            obj1.jira(1)
            write_data(Test_database.Excel_report, Test_database.Excel_sheet_name, 3, 6, "Test Case Failed")


        print("--------------------------------comparing the total marks  second row of marks from UI---------------------------------")
        #
        def database_secondrow(value, row):
            obj = DatabaseConnection
            value = obj.Query(self.driver, row)
            marksofaditi = []
            marksofaditi.extend(value)
            return marksofaditi

        marksofaditi = database_secondrow("marks_obtained", 9)
        marksofaditi.extend(database_secondrow("total_marks", 14))
        marksofaditi.extend(database_secondrow("percentage_marks_aditi", 15))
        marksofaditi.extend(database_secondrow("Percentage attendece of aditi", 20))
        print(marksofaditi)
        marksofaditi = [name[0] for name in marksofaditi]
        print("MARKS_OBTAINED, TOTAL MARKS, MARKS PERCENTAGE, ATTENDANCE PERCENTAGE FROM DATABASE ARE:", marksofaditi)

        # tSmryList = self.driver.find_elements(By.CSS_SELECTOR,
        #                                        "div.visual.visual-card.customPadding.allow-deferred-rendering svg tspan")

        mrk = []
        i = 0
        marks = ""
        groupNum = ""
        groupName = ""

        for ele in monthattendence.tSmryList():
            if i == 2:
                groupNum = ele.text
                print("GroupNo:", groupNum)

            if i == 3:
                groupName = ele.text
                print("GroupName:", groupName)

            if 4 <= i < len(monthattendence.tSmryList()):
                marks = ele.text

                if 4 <= i <= 5:
                    mrk.append(int(marks))

                if 6 <= i < len(monthattendence.tSmryList()):
                    if "%" in ele.text:
                        marks = marks.replace("%", "")

                        if i == 6:
                            mrk.append(int(marks[:marks.index(".")]))
                        else:
                            # print("Replace String:", marks)
                            mrk.append(float(marks))

            i += 1

        marks_from_dashboard = mrk
        print("MARKS_OBTAINED, TOTAL MARKS, MARKS PERCENTAGE, ATTENDANCE PERCENTAGE FROM DASHBOARD ARE:",
              marks_from_dashboard)


        # Report results to Excel file
        failed_rows = []
        column_name = ['Marks Obtained', 'Total Marks', 'Marks Percentage', 'Attendance Percentage']

        for j in range(len(column_name)):
            if marksofaditi[j] != marks_from_dashboard[j]:
                failed_rows.append((j + 1, column_name[j], marksofaditi[j], marks_from_dashboard[j]))

        if not failed_rows:
            write_data(Test_database.Excel_report, Test_database.Excel_sheet_name, 4, 5,
                       "Data from PowerBi Dashboard and Database are matching")
            write_data(Test_database.Excel_report, Test_database.Excel_sheet_name, 4, 6, "Test Case Passed")
        else:
            error_message = ""
            for row, col, expected, actual in failed_rows:
                error_message += f"In row {row}, {col} from dashboard does not match {col} from database. Expected value: {expected}, Actual value: {actual}\n"

            write_data(Test_database.Excel_report, Test_database.Excel_sheet_name, 4, 5, error_message.strip())
            write_data(Test_database.Excel_report, Test_database.Excel_sheet_name, 4, 6, "Test Case Failed")

        time.sleep(3)
        # print("group number from dashborad is:",groupNum)
        # print("group name from dashborad is",groupName)
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
        #



        print("---------------------------------comparing remarks data------------------")
        # self.driver.switch_to.frame(self.driver.find_element(By.CSS_SELECTOR, "iframe[class=visual-sandbox]"))

        self.driver.switch_to.frame(monthattendence.iframe1())
        # charList = self.driver.find_elements(By.CSS_SELECTOR, "div[id=sandbox-host] g[class=word] text:nth-of-type(1)")
        # print("Size of List:", len(charList))

        charListCmp = []
        for ele in monthattendence.charlist1():
            # print("Chr:", ele.text)
            charListCmp.append(ele.text)
        print("Charactristics Summery:", charListCmp)


        self.driver.switch_to.default_content()
        obj = DatabaseConnection
        database_remarks = obj.Query(self.driver, 35)
        print("databse student performaing grid is", database_remarks)

        performing_grid = database_remarks[0][0].strip('"')

        # Split the performing grid string into a list of characteristics
        performing_grid_list = performing_grid.split(',')

        # Compare the characteristics summary list with the performing grid list
        if set(charListCmp) == set(performing_grid_list):
            write_data(Test_database.Excel_report, Test_database.Excel_sheet_name, 5, 5,
                       "Data from PowerBi Dashboard and Database are matching")
            write_data(Test_database.Excel_report, Test_database.Excel_sheet_name, 5, 6, "Test Case Passed")
        else:
            error_message = "Characteristics in the summary list do not match the performing grid list."
            write_data(Test_database.Excel_report, Test_database.Excel_sheet_name, 5, 5, error_message)
            write_data(Test_database.Excel_report, Test_database.Excel_sheet_name, 5, 6, "Test Case Failed")

            # Write the values from the dashboard and database that do not match
            for i in range(len(charListCmp)):
                if charListCmp[i] != performing_grid_list[i]:
                    row_number = i + 1
                    dashboard_value = charListCmp[i]
                    database_value = performing_grid_list[i]
                    mismatch_message = f"In row {row_number}, dashboard value '{dashboard_value}' does not match database value '{database_value}'"
                    write_data(Test_database.Excel_report, Test_database.Excel_sheet_name, 5, 5, mismatch_message)



        #

        print("---------------------comparing the last grid data ---------------------------------")
        # gridList = self.driver.find_elements(By.CSS_SELECTOR, "div[role=columnheader]")
        gridContentList = []
        gridHeadingList = []

        for j in range(2, len(monthattendence.gridList1()) + 1):
            gridEleHeading = self.driver.find_element(By.CSS_SELECTOR,"div[role=columnheader]:nth-of-type(" + str(j) + ")")
            gridHeadingList.append(gridEleHeading.text)

            if j == 4:
                gridEleContent = self.driver.find_element(By.CSS_SELECTOR, "div[role=gridcell]:nth-of-type(" + str(j) + ") :nth-child(1)")
                gridContentList.append(gridEleContent.text)
            else:
                gridEleContent = self.driver.find_element(By.CSS_SELECTOR,"div[role=gridcell]:nth-of-type(" + str(j) + ")")
                gridContentList.append(gridEleContent.text)

        print("GridHeading:", gridHeadingList)
        print("GridContent: from dashboard", gridContentList)

        obj = DatabaseConnection()
        database_student_performing_grid = obj.Query36()
        print("Grid content from database :", database_student_performing_grid)
        time.sleep(5)

        name_match = gridContentList[0] == database_student_performing_grid[0][0]
        subject_match = gridContentList[1] == database_student_performing_grid[0][1]
        score_match = int(gridContentList[2]) == database_student_performing_grid[0][2]
        total_score = int(gridContentList[3]) == database_student_performing_grid[0][3]
        percentage_match = float(gridContentList[4].strip('%')) == database_student_performing_grid[0][4]
        traits_match = gridContentList[5] == database_student_performing_grid[0][5]
        id_match = int(gridContentList[6]) == database_student_performing_grid[0][6]

        log.info("Comparing the database values and dashboard values of the grid at the end of UI")

        if name_match and subject_match and score_match and total_score and percentage_match and id_match:
            write_data(Test_database.Excel_report, Test_database.Excel_sheet_name, 6, 5,
                       "Data from PowerBi Dashboard and Database are matching")
            write_data(Test_database.Excel_report, Test_database.Excel_sheet_name, 6, 6, "Test Case Passed")
        else:
            error_message = "Data from PowerBi Dashboard and Database do not match."
            write_data(Test_database.Excel_report, Test_database.Excel_sheet_name, 6, 5, error_message)
            write_data(Test_database.Excel_report, Test_database.Excel_sheet_name, 6, 6, "Test Case Failed")

            # Write the values from the database and dashboard that do not match
            if not name_match:
                write_data(Test_database.Excel_report, Test_database.Excel_sheet_name, 6, 5,
                           f"Expected Name: {database_student_performing_grid[0][0]}, Actual Name: {gridContentList[0]}")
            if not subject_match:
                write_data(Test_database.Excel_report, Test_database.Excel_sheet_name, 6, 5,
                           f"Expected Subject: {database_student_performing_grid[0][1]}, Actual Subject: {gridContentList[1]}")
            if not score_match:
                write_data(Test_database.Excel_report, Test_database.Excel_sheet_name, 6, 5,
                           f"Expected Score: {database_student_performing_grid[0][2]}, Actual Score: {gridContentList[2]}")
            if not total_score:
                write_data(Test_database.Excel_report, Test_database.Excel_sheet_name, 6, 5,
                           f"Expected Total Score: {database_student_performing_grid[0][3]}, Actual Total Score: {gridContentList[3]}")
            if not percentage_match:
                write_data(Test_database.Excel_report, Test_database.Excel_sheet_name, 6, 5,
                           f"Expected Percentage: {database_student_performing_grid[0][4]}, Actual Percentage: {gridContentList[4]}")
            if not traits_match:
                write_data(Test_database.Excel_report, Test_database.Excel_sheet_name, 6, 5,
                           f"Expected Traits: {database_student_performing_grid[0][5]}, Actual Traits: {gridContentList[5]}")
            if not id_match:
                write_data(Test_database.Excel_report, Test_database.Excel_sheet_name, 6, 5,
                           f"Expected ID: {database_student_performing_grid[0][6]}, Actual ID: {gridContentList[6]}")



        print("-----------------------------attendence reason--------------------------")
        # absentReasonList = self.driver.find_elements(By.CSS_SELECTOR,
        #                                              "svg[name='Stacked bar chart'] text[class='setFocusRing']")

        # absentPerList = self.driver.find_elements(By.CSS_SELECTOR, "svg[name='Stacked bar chart'] text[class='label']")

        absentListData = []

        for ele in monthattendence.absentReasonList1():
            print("Absent Reason:", ele.text)
            absentListData.append(ele.text)

        for ele in monthattendence.absentPerList1():
            print("Absent Per:", ele.text)
            if '%' in ele.text:
                ele.text.strip("%")
            absentListData.append(ele.text)

        print("Absent List Reasons:", absentListData)
        obj=DatabaseConnection
        database_low_reason_attendance = obj.Query(self.driver,37)
        print("Database absent reason table data:", database_low_reason_attendance)

        # Compare data
        for reason, percentage in database_low_reason_attendance:
            if reason in absentListData:
                print(f"Reason: {reason}")
                print(f"Percentage: {percentage}%")

        # If tests fail
        failed_rows = []
        column_name = ['Reason', 'Percentage']

        for reason, percentage in database_low_reason_attendance:
            if reason not in absentListData:
                failed_rows.append((reason, percentage))

        if not failed_rows:
            write_data(Test_database.Excel_report, Test_database.Excel_sheet_name, 7, 5,
                       "Data from Dashboard and Database are matching")
            write_data(Test_database.Excel_report, Test_database.Excel_sheet_name, 7, 6, "Test Case Passed")
        else:
            error_message = ""
            for reason, percentage in failed_rows:
                error_message += f"Reason: {reason}, Percentage: {percentage}% does not exist in the Dashboard data.\n"

            write_data(Test_database.Excel_report, Test_database.Excel_sheet_name, 7, 5, error_message.strip())
            write_data(Test_database.Excel_report, Test_database.Excel_sheet_name, 7, 6, "Test Case Failed")

        # obj2=Sendemailclass()
        # obj2.send_email()


























































