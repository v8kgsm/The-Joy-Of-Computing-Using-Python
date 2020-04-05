# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 17:39:34 2020

@author: Vikas Tiwari
"""
'''
If your underlying os is windows:

You have to download chromedriver_win32.zip from the ChromeDriver Download Location and unzip it for usage.
Additionally, if you are explicitly specifying the Chromedriver binary path you have to append the binary extension as well, effectively i.e. chromedriver.exe.
While mentioning the Chromedriver binary path you have to either use the single forward slash i.e. (/) along with the raw (r) switch or you have to use the escaped backslash i.e. (\\).
So your effective line of code will be :

driver = webdriver.Chrome(executable_path=r'C:/path/to/chromedriver.exe')
If your underlying os is linux:

You have to download chromedriver_linux64 from the ChromeDriver Download Location and untar it for usage.
Additionally, if you are explicitly specifying the Chromedriver binary path you don't have to provide any extension for the executable binary, effectively i.e. chromedriver.
While mentioning the Chromedriver binary path you have to use the single forward slash i.e. (/).
So your effective line of code will be :

driver = webdriver.Chrome(executable_path='/path/to/chromedriver')
If your underlying os is macos:

You have to download chromedriver_mac64 from the ChromeDriver Download Location and untar it for usage.
Additionally, if you are explicitly specifying the Chromedriver binary path you don't have to provide any extension for the executable binary, effectively i.e. chromedriver.
While mentioning the chromedriver binary path you have to use the single forward slash i.e. (/).
So your effective line of code will be :

driver = webdriver.Chrome(executable_path='/path/to/chromedriver')

'''
#steps
"""
step 1 :
    to open browser :
    driver = webdriver.Chrome(executable_path=r'C:/Users/user/Downloads/chromedriver.exe')
step 2:
    to load page :
    driver.get("https://www.seleniumhq.org")
step 3:
    to locate  a element in the page like Downloads
    elem=driver.find_element_by_link_text("Downloads")
step 4:
    to click the element
    elem.click()
    
To find something in the search bar using automation
step1: find the search bar id by inspect mode
step2: search = browser.find_element_by_id('id')
step3: search.send_keys('write what u want to search.')


'''



































        
