# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 11:36:29 2020

@author: user
"""

import matplotlib.pyplot as p
#p.plot([1,2,3,4,5,6,7,8],[1,4,9,16,25,36,49,64])
#p.plot([x],[y])
#when x value is not passed then python takes it default
p.ylabel("Squares")
p.xlabel("Integers")

#p.plot([1,2,3,4,5,6,7,8],[1,4,9,16,25,36,49,64],'ro')
#p.plot([1,2,3,4,5,6,7,8],[1,4,9,16,25,36,49,64],'r--')
#p.plot([1,2,3,4,5,6,7,8],[1,4,9,16,25,36,49,64],'bs')
p.plot([1,2,3,4,5,6,7,8],[1,4,9,16,25,36,49,64],'g^')