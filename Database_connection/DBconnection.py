import openpyxl
import pyodbc

import DBConfigurations.Config_file

# cnxn_str = ("Driver={SQL Server};"
#             "Server=RLPT-0015\SQLEXPRESS;"
#             "Database=POC2;"
#             "Trusted_Connection=yes;")
cnxn_str = DBConfigurations.Config_file.connection_string
my_cnxn = pyodbc.connect(cnxn_str)

cursor = my_cnxn.cursor()

#cursor.execute('select Customer_Segment as'Customer Segment',Product_Category as 'Product Category',ROUND(sum(unit_Price),2) "Sum of Unit Price" from Superstoretestinggroup by Customer_Segment, Product_Categoryorder by Customer_Segment, Product_Category asc')

book=openpyxl.load_workbook(DBConfigurations.Config_file.Excel_Report_File)
sheet=book.active
cell=sheet.cell(row=2,column=3)
print(cell.value)  #qurry

db_list123=[]
cursor.execute(cell.value)
for i in cursor:
    db_list123.append(i)

print("db_list123:",db_list123)