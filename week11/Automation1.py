# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 18:34:23 2020

@author: Vikas Tiwari
"""

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions  as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path=r'C:/Users/user/Downloads/chromedriver.exe')
driver.get("https://web.whatsapp.com/")
wait=WebDriverWait(driver,600)
target='"Mø_tØ"'
string="Message sent via Python using Chrome."
x_arg='//span[contains(@title,'+ target +')]'
target=wait.until(EC.presence_of_element_located((By.XPATH, x_arg)))
target.click()

input_box=driver.find_element_by_class_name('1Plpp')
for i in range(50):
    input_box.send_keys(string+Keys.ENTER)

#youtube
#    
#name=input("Enter the name of user or group:")
#msg=input("Enter your ,message:")
#count=int(input("Enter the count:"))
#input("Enter anything after scanning QR code:")
# 
#user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
#user.click()
#
#msg_box = driver.find_element_by_class_name('inupt-container')
#for i in range(count):
#    msg_box.send_keys(msg)
#    button = driver.find_element_by_class_name('compose-btn-send')
#    button.click()