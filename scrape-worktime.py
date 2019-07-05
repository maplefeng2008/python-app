#!/usr/bin/env python3

import requests
import time
import datetime
import sys
from selenium import webdriver
from bs4 import BeautifulSoup

options = webdriver.chrome.options.Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
chromedriver = "/usr/local/chromedriver-Linux64"

browser = webdriver.Chrome(executable_path=chromedriver, chrome_options=options)
browser.get("http://time.nec.cn:8080/iclock/accounts/login")

username = browser.find_element_by_id("id_username");
password = browser.find_element_by_id("id_password");
login = browser.find_element_by_id("id_login_btn");
username.clear()
#xxxxxxxx00782
username.send_keys(sys.argv[1])
password.clear()
password.send_keys(sys.argv[1])
login.click()
time.sleep(5)

print("-----------------------")
bsObj = BeautifulSoup(browser.page_source, "lxml")
childrenList = bsObj.find("div", {"class":"cont"}).findAll('tr')
time = datetime.datetime.now()
lateTimes = "-1"
for children in childrenList:
    for td in children.findAll('td'):
        if len(td.getText()) == 19:
            if lateTimes == "-1":
                lateTimes = ""
                print("id  : " + sys.argv[1])
                print("from: " + td.getText() + "\n")
                print("last 7 days: ")
            dbtime = datetime.datetime.strptime(td.getText(),'%Y-%m-%d %H:%M:%S')
            if dbtime.hour >= 9 and dbtime.hour < 11:
                lateTimes += td.getText() + '\n'
            if (time - dbtime).days < 7:
                print(td.getText())
print("\nlate days: \n" + lateTimes)
print("-----------------------")

browser.quit()
