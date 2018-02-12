# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 16:20:46 2018

@author: Wey Yi
"""

#(Financials: currency exchange) Write a program that prompts the user to enter
#the currency exchange rate between U.S. dollars and Chinese Renminbi (RMB).
#Prompt the user to enter 0 to convert from U.S. dollars to Chinese RMB and 1 for
#vice versa. Prompt the user to enter the amount in U.S. dollars or Chinese RMB to
#convert it to Chinese RMB or U.S. dollars, respectively.

def Exchange(amt):
    if n == 0:
        Exch = amt * USD2RMB
        print('You will get RMB', Exch)
    elif n == 1:
        Exch = amt * RMB2USD
        print('You will get USD', Exch)
    else:
        print('Error: Please let a valid value of either 0 or 1 to indicate what you\'d like to convert')

USD2RMB = 6.33
RMB2USD = 0.16
n = eval(input('Enter 0 for USD to RMB, or 1 for RMB to USD: '))
amt = eval(input('Enter the amount you\'d like to convert: '))
Exchange(amt)