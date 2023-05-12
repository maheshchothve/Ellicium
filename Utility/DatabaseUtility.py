import openpyxl
import pyodbc

import DBConfigurations.Config_file


class DatabaseConnection:
    def Query1(self):

        cnxn_str = ("Driver={SQL Server};""Server=RLPT-0015\SQLEXPRESS;""Database=POC2;""Trusted_Connection=yes;")

        my_cnxn = pyodbc.connect(cnxn_str)

        cursor = my_cnxn.cursor()
        book = openpyxl.load_workbook(DBConfigurations.Config_file.Excel_Report_File)
        sheet = book.active
        cell = sheet.cell(row=2, column=3)

        cursor.execute(cell.value)
        print(cell.value)
        db_list1 = []

        for i in cursor:
            db_list1.append(i)
        #
        #
        print("list1",db_list1)

        return db_list1

    def Query2(self):

        cnxn_str = ("Driver={SQL Server};""Server=RLPT-0015\SQLEXPRESS;""Database=POC2;""Trusted_Connection=yes;")

        my_cnxn = pyodbc.connect(cnxn_str)

        cursor = my_cnxn.cursor()
        book = openpyxl.load_workbook(DBConfigurations.Config_file.Excel_Report_File)
        sheet = book.active
        cell = sheet.cell(row=3, column=3)

        cursor.execute(cell.value)
        print(cell.value)
        db_list2 = []

        for i in cursor:
            db_list2.append(i)
        #
        #
        print("list2",db_list2)

        return db_list2



