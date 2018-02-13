# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 19:01:00 2018

@author: Wey Yi
"""

#(Science: wind-chill temperature) Exercise 2.9 gives a formula to compute the
#wind-chill temperature. The formula is valid for temperatures in the range
#between -58°F and 41°F and for wind speed greater than or equal to 2. Write a
#program that prompts the user to enter a temperature and a wind speed. 
#The program displays the wind-chill temperature if the input is valid; 
#otherwise, it displays a message indicating whether the temperature and/or 
#wind speed is invalid.


def windchill(ta, v):
    if (-58 <= ta <= 41) and (v >= 2):
        twc = 35.74 + (0.6215 * ta) - (35.75 * v ** 0.16) + (0.4275 * ta * v ** 0.16)
        print("The windchill temperature is", twc)
    else:
        print('invalid input')
    

ta = eval(input('What is the outside temperature?: '))
v = eval(input('What is the wind speed?: '))
twc = windchill(ta, v)