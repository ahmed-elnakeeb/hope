#import pandas as pd
#pd.read_excel('data.xlsx', index_col=0)  
#df = excel.read_excel("./data.xlsx") 
#df.to_csv("./data.csv", sep=",")
import io
import xlrd
import csv

def csv_from_excel():
    wb = xlrd.open_workbook('data.xlsx')
    sh = wb.sheet_by_name('Sheet1')
    your_csv_file = open('your_csv_file.csv', 'w',encoding="utf=8")
    wr = csv.writer(your_csv_file, quoting=csv.QUOTE_ALL)

    for rownum in range(sh.nrows):
        print(sh.row(rownum))
        wr.writerow(sh.row_values(rownum,end_colx=3))

        

    your_csv_file.close()
csv_from_excel()