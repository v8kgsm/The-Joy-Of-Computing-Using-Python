# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 15:55:59 2020

@author: user
"""

from datetime import datetime as d
import pytz

timezones=pytz.all_timezones
for i in range(len(timezones)):
    zone=timezones[i]
    tz=pytz.timezone(zone)
    print("current time at zone", zone,' is', d.now(tz))
    
    