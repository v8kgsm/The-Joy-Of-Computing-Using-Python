# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 20:02:43 2020

@author: Vikas Tiwari
"""
'''
calender
datetime
pytz = tz is time Zone.
'''

'''
packages
1) current time : from datetime import datetime
    print(datetime.now())  #system time
@@@ generally in databases datetime is stored as year-month-date
2) import pytz
    tz=pytz.timezone('Singapore')
    print(d.now(tz))
    
3) to get list of timezone
    pytz.all_timeszones

4) import calendar
    calendar.weekday?   #to check the functioning of any function put ? after the function.
    