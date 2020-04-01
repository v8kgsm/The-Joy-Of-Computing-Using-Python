# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 18:40:16 2020

@author: user
"""

import random
import datetime
birthday=[]
i=0
while(i<50):
    year = random.randint(1895,2019)
#    print(year)
    if(year%4==0 and year%100!=0 or year%400==0):
        leap=1
    else:
        leap=0
    month=random.randint(1,12)
    if(month==2 and leap==1):
        day=random.randint(1,29)
    elif(month==2 and leap==0):
        day=random.randint(1,28)
    elif(month==7 or month==8):
        day=random.randint(1,31)
    elif(month%2!=0 and month<7):
        day=random.randint(1,31)
    elif(month%2==0 and month>7 and month<12):
        day=random.randint(1,31)
    else:
        day=random.randint(1,30)
    dd=datetime.date(year,month,day)
    day_of_year=dd.timetuple().tm_yday
    i=i+1
    birthday.append(day_of_year)
    
birthday.sort()
i=0
while(i<50):
    print(birthday[i])
    i+=1
    
    
    
#datetime.date.today()
#Out[3]: datetime.date(2020, 3, 24)
    
#datetime.date.today().strftime("%Y")
#Out[5]: '2020'
#    
#datetime.date.today().strftime("%B")
#Out[6]: 'March'
#
#datetime.date.today().strftime("%d")
#Out[7]: '24'
#
#datetime.date.today().strftime("%W")
#Out[8]: '12'
#    
#print("Week Number of the month:",datetime.date.today().strftime("%W"))
#Week Number of the month: 12
#
#print("Weekday of the week:",datetime.date.today().strftime("%w"))
#Weekday of the week: 2
#
#print("Day of the year:",datetime.date.today().strftime("%j"))
#Day of the year: 084
#
#print("Day of the Week:",datetime.date.today().strftime("%A"))
#Day of the Week: Tuesday
#
#datetime.datetime.now()
#Out[13]: datetime.datetime(2020, 3, 24, 22, 34, 12, 612104)    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    