#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 14:15:10 2020
Exercise 5.2- fermat proof 
@author: Aaron Etienne (aetienne)
"""

#Define fermat's equation a^n + b^n = c^n
def fermat(a, b, c, powerN):
    N = powerN;
    #N has to be higher than power of 2     
    while N <= 2:
        N = int(input("Please enter power > 2: \n"));
    #Nested if statement defining equation 
    if (a**N) + (b**N) == (c**N):
        print("Holy smokes Fermat was wrong!!");
    #specify different output 
    else:
        print("Fermat was right- Yours doesn't work!");
#create variable for input values 
a = int(input("Enter x value: \n"));
b = int(input("Enter y value: \n"));
c = int(input("Enter z value: \n"));
powerN = int(input("Enter power: \n"));

fermat(a, b, c, powerN);