
import xlrd
import xlwt

file_location = (r'C:\\Users\Griffin\Documents\PythonProjects\Selenium-Talkdesk\Scripts\csv\sample_data.xlsx')
workbook = xlrd.open_workbook(file_location)

sheet = workbook.sheet_by_index(0)
sheet.cell_value(0, 0)
sheet.nrows
sheet.ncols

for col in range(sheet.ncols):
    print (sheet.cell_value(0, col))



