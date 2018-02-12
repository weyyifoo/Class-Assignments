# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 10:14:29 2018

@author: Wey Yi
"""

# code finds the smallest number of the user inputs

b = 999999999999999999999

for i in range(5):
    a = eval(input('enter number: '))
    if a < b:
        b = a
        print('current smallest number updated to: ', b)
    else:
        print('current smallest number: ', b)