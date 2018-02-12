# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 15:58:18 2018

@author: Wey Yi
"""

#(Sort three integers) Write a program that prompts the user to enter three integers
#and displays them in increasing order

def order(m, n, o):
    S = [0, 0, 0] # initialize list
    if (m > n) and (m > o):
        S[2] = m
    elif (m > n) and (m < o):
        S[1] = m
    elif (m < n) and (m > o):
        S[1] = m
    elif (m < n) and (m < o):
        S[0] = m
    
    if (m < n) and (n > o):
        S[2] = n
    elif (m > n) and (n > o):
        S[1] = n
    elif (m < n) and (n < o):
        S[1] = n
    elif (m > n) and (n < o):
        S[0] = n
        
    if (o > n) and (m < o):
        S[2] = o
    elif (o > n) and (m > o):
        S[1] = o
    elif (o < n) and (m < o):
        S[1] = o
    elif (o < n) and (m > o):
        S[0] = o
    return S
    
    
m = eval(input('Enter test number 1: '))
n = eval(input('Enter test number 2: '))
o = eval(input('Enter test number 3: '))

#order(m, n, o)
print(order(m, n, o))