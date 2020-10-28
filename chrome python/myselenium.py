from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pandas
import os
import csv
    
def getname(sku):
    browser = webdriver.Chrome()
    browser.get('https://www.ubuy.com.kw/ar/?q='+sku)
    timecomm=0
    while True:
        try:
            a=browser.find_element_by_class_name("ais-hits--item")
            if len(a.text)>0:
                break
            
        except:
            time.sleep(.1)
            timecomm+=0.1
        if timecomm>30:
            browser.close()
            return "null"        
    x=a.text.split("\n")[0]    
    browser.close()
    return(x)


file = open("./name.csv", "r",encoding="utf-8")
reader = csv.reader(file, delimiter=',')
prv=0
for row in reader:
    if row[0]==str(prv)or row[0]=="SKU":
        print(prv)
        break
    prv=row[0]
    print(row[3])
    x=getname(row[3])
    print(x)


