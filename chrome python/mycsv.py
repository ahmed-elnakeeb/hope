import pandas
import os
import csv

file = open("./name.csv", "r",encoding="utf-8")
reader = csv.reader(file, delimiter=',')
prv=0
for row in reader:
    if row[0]==str(prv):
        print(prv)
        break
    prv=row[0]



# file=pandas.read_csv("name.csv",sep=",",encoding="utf-8")
# print(file.columns[0:8])
# print(file.columns[0:8])
