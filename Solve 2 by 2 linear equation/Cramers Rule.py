# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 13:47:44 2018

@author: Wey Yi
"""

#(Algebra: solve linear equations) You can use Cramer’s rule to solve the
#following system of linear equation:
#Write a program that prompts the user to enter a, b, c, d, e, and f and display the
#result. If ad – bc is 0, report that The equation has no solution.

def solvex(a, b, c, d, e, f):
    if ((a*d - b*c) == 0):
        print('The equation has no solution')
    else:
        x = ((e*d) - (b*f))/((a*d) - (b*c))
    return x
    
def solvey(a, b, c, d, e, f):
    if ((a*d - b*c) == 0):
        print('The equation has no solution')
    else:
        y = ((a*f - e*c)/(a*d - b*c))
    return y

a = eval(input('Enter the value for a: '))
b = eval(input('Enter the value for b: '))
c = eval(input('Enter the value for c: '))
d = eval(input('Enter the value for d: '))
e = eval(input('Enter the value for e: '))
f = eval(input('Enter the value for f: '))

x = solvex(a, b, c, d, e, f)
y = solvey(a, b, c, d, e, f)

print('the value of x is: ', x)
print('the value of y is: ', y)