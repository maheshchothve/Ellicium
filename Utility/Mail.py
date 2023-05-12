import datetime
import os

import win32com.client as win32

import Ellicium.DBConfigurations.Config_file


class Sendemailclass:
    def send_email(self):
        # Get the email addresses from Sheet2, column A
        wb = win32.gencache.EnsureDispatch('Excel.Application')
        wb.Visible = False
        wb.Workbooks.Open(os.path.abspath(Ellicium.DBConfigurations.Config_file.Excel_Report_File))

        ws = wb.Worksheets('Sheet2')
        rngTo = ws.Range("A1:A" + str(ws.Cells(ws.Rows.Count, "A").End(-4162).Row))
        strTo = ""
        for cel in rngTo:
            strTo = strTo + cel.Value + ";"
            cel = None

        # Get the project name from Sheet2, column B
        projName = ws.Range("B1").Value

        # Get the counts for pass and fail from Sheet1, column B
        ws = wb.Worksheets('Sheet1')
        passCount = ws.Evaluate('COUNTIF(F:F,"Test Case Passed")')
        failCount = ws.Evaluate('COUNTIF(F:F,"Test Case Failed")')

        # Get the count of rows in Sheet1, column A
        rowCount = ws.Cells(ws.Rows.Count, "A").End(-4162).Row - 1

        # Create the email body as an HTML table
        strBody = "<html><body><p>Hi," \
                  "</p><p>Please find the below attached excel sheet for more details." \
                  "</p><p>Here is an update on " + projName + ":</p><table border='1'><tr><th>Total number of Testcases</th><th>Total number of Testcase passed</th><th>Total number of Testcase failed</th></tr><tr><td>" + str(
            rowCount) + "</td><td>" + str(passCount) + "</td><td>" + str(failCount) + "</td></tr></table></body></html>"

        # Get the attachment file name
        strAttachment = Ellicium.DBConfigurations.Config_file.Excel_Report_File

        # Create the Outlook object and email
        outlook = win32.Dispatch('Outlook.Application')
        mail = outlook.CreateItem(0)
        mail.To = strTo
        mail.Subject = projName + " - " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        mail.HTMLBody = strBody
        mail.Attachments.Add(os.path.abspath(strAttachment))
        # mail.Display(False)
        mail.Send()
        try:
            wb.Quit()
        except:
            pass