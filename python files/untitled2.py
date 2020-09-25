# -*- coding: utf-8 -*-
"""
Created on Fri May 22 14:17:04 2020

@author: Meghana
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
import time
stops=[]
stops=[['75.149295','15.350276','Railway Station Hubli'],
       ['75.146354','15.353492','Dr. B R Ambedkar Circle'],
       ['75.136132','15.350821','OBS'],
       ['75.130337','15.356087','Hosur Stop'],
       ['75.127149','15.361844','KIMS Stop'],
       ['75.124662','15.365462','Vidhyanagar Stop'],
       ['75.121109','15.369146','BVB College Stop'],
       ['75.118897','15.371473','Unkal Cross Stop'],
       ['75.111255','15.383753','Unkal lake Stop'],
       ['75.105625','15.388923','Bairidevarkoppa Stop'],
       ['75.082968','15.398617','Navanagar Stop'],
       ['75.053876','15.416518','Navaloor Station Stop'],
       ['75.048178','15.418650','SDM'],
       ['75.042145','15.419943','Sattur Stop'],
       ['75.019002','15.439146','Gandhinagar Stop'],
       ['75.009048','15.461033','Dharwad'],
       ]
for i in range(0,len(stops)):
    for j in range(0,3):
        print(i,stops[i][j])
for i in range(len(stops)-2, -1, -1):   
    for j in range(0,3):
        print(i,stops[i][j]) 
        
while(1):
    for i in range(0,len(stops)):
#        browser = webdriver.Chrome(ChromeDriverManager().install())
        browser = webdriver.Chrome(r'chromedriver')
        browser.get("ec2-13-233-84-121.ap-south-1.compute.amazonaws.com:3000/form")
#        browser.get("localhost:5000/form")
        userElem = browser.find_element_by_id("lat")
        userElem.send_keys(stops[i][1])  #latitude here
        passwordElem = browser.find_element_by_id('lon')
        passwordElem.send_keys(stops[i][0])  #longitude here
        positionElem = browser.find_element_by_id('disc')
        positionElem.send_keys(stops[i][2])  #discription here
        loginElem = browser.find_element_by_id('btnlogin')
        loginElem.click()
        time.sleep(7)
        browser.quit()
        x=stops[i][1]
        y=stops[i][0]
        time.sleep(2)
        print(x,y)
    for i in range(len(stops)-2, -1, -1):
#        browser = webdriver.Chrome(ChromeDriverManager().install())
        browser = webdriver.Chrome(r'chromedriver')
        browser.get("ec2-13-233-84-121.ap-south-1.compute.amazonaws.com:3000/form")
#        browser.get("localhost:5000/form")
        userElem = browser.find_element_by_id("lat")
        userElem.send_keys(stops[i][1])  #latitude here
        passwordElem = browser.find_element_by_id('lon')
        passwordElem.send_keys(stops[i][0])  #longitude here
        positionElem = browser.find_element_by_id('disc')
        positionElem.send_keys(stops[i][2])  #discription here
        loginElem = browser.find_element_by_id('btnlogin')
        loginElem.click()
        time.sleep(7)
        browser.quit()
        x=stops[i][1]
        y=stops[i][0]
        time.sleep(2)
        print(x,y)