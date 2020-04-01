# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 21:58:08 2020

@author: user
"""

import random
import matplotlib.pyplot as plt
account=0
x=[]
y=[]
for i in range(365):
    # range contains number of days for which the user is playing the game.
    x.append(i+1)
    bet = random.randint(1,10)
    lucky_draw = random.randint(1,10)
#    print("Bet:",bet)
#    print("Lucky_draw:",lucky_draw)
    if(bet==lucky_draw):
        account=account+900-100
    else:
        account=account-100
    y.append(account)
print("Total Amount in your gambling account:",account)
plt.plot(x,y,"b-")
plt.show()