# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 14:56:36 2020

@author: Vikas Tiwari
"""
#code to print day with respect to given date(d/m/y)

import calendar

def get_day(day_index):
    list_of_days=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    return list_of_days[day_index]

def check_leap(y):
    if(y%100==0):
        if(y%400==0):
            return True
        else:
            return False
    else:
        if(y%4==0):
            return True
        else:
            return False
        
def check_valid_date(d,m,y,l):
    if l:
        if m==2:
            if d<30:
                return True
            else:
                return False
        else:
            if m<8:
                if m%2==1:
                    if d<32:
                        return True
                    else:
                        return False
                else:
                    if d<31:
                        return True
                    else:
                        return False 
            else:
                if m%2==0:
                    if d<32:
                        return True
                    else:
                        return False
                else:
                    if d<31:
                        return True
                    else:
                        return False
    else:
        if m==2:
            if d<28:
                return True
            else:
                return False
        else:
            if m<8:
                if m%2==1:
                    if d<32:
                        return True
                    else:
                        return False
                else:
                    if d<31:
                        return True
                    else:
                        return False 
            else:
                if m%2==0:
                    if d<32:
                        return True
                    else:
                        return False
                else:
                    if d<31:
                        return True
                    else:
                        return False


while(1):
    year=int(input("Enter the Year (1970-2020)?"))
    if(year<1970 or year>2020):
         print("Enter the Year with in the range :) ")
    else:
        break
while(1):
    month=int(input("Enter the Month(1-12)?"))
    if(month<=12 and month >=1):
         break
    else:
        print("Enter the Month with in the range :) ")

    
leap = check_leap(year)

while(1):
    date=int(input("Enter Date?"))
    if(date >0 and check_valid_date(date,month,year,leap)):
         break
    else:
        print("Enter a valid date :) ")


    
day_index=calendar .weekday(year,month,date)
day=get_day(day_index)
    
print(date,'/',month,'/',year,' falls on', day)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    