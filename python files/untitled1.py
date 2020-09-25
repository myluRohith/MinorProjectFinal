# -*- coding: utf-8 -*-
"""
Created on Wed May 20 22:41:55 2020

@author: Meghana
"""

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

while(1):
    print("Enter RFID")
    rfid=int(input())
    print(rfid)
    
    print("Destination  Ticket Price")
    print("Station1     Rs.5")
    print("Station2     Rs.8")
    print("Station3     Rs.10")
    print("Station4     Rs.15")
    print("Enter Choice")
    key=int(input())
    print(key)
    
    #browser = webdriver.Chrome(executable_path='C:\Users\Meghana\Desktop\chromedriver.exe')
    #browser = webdriver.Chrome(ChromeDriverManager().install())
    browser = webdriver.Chrome(r'chromedriver')
    #browser = webdriver.Chrome(ChromeDriverManager().install())
    #browser = webdriver.Chrome()
    #browser.get("http://localhost:5000/ticket")
    browser.get("ec2-13-233-84-121.ap-south-1.compute.amazonaws.com:3000/ticket")
    userElem = browser.find_element_by_id("rfid")
    userElem.send_keys(rfid)  #admn no here
    passwordElem = browser.find_element_by_id('key')
    passwordElem.send_keys(key)  #password here
    loginElem = browser.find_element_by_id('btnlogin')
    loginElem.click()
    browser.quit()
