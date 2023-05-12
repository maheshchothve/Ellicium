from turtle import pd

from jira import JIRA, JIRAError
import pandas as pd
import Ellicium.DBConfigurations.Config_file


class JiraMethod :
    def jira(self,row_number):
        options = {
            'server': 'https://cogniwizetrainings.atlassian.net'
        }
        jira = JIRA(options, basic_auth=(
            Ellicium.DBConfigurations.Config_file.jira_Mail, Ellicium.DBConfigurations.Config_file.jira_API_key))
        # read description from Excel sheet
        df = pd.read_excel(Ellicium.DBConfigurations.Config_file.Excel_Report_File)
        description = df.loc[row_number, ' Actual output']
        # create Jira issue
        new_issue = {
            'project': {'key': 'E1'},
            'summary': 'Dashborad data and database data are not matching',
            'description': description,
            'issuetype': {'name': 'Bug'},
        }
        try:
            issue = jira.create_issue(fields=new_issue)
            print(f"Successfully created issue {issue.key}")
        except JIRAError as e:
            print(f"Failed to create issue: {e}")
