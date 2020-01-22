#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 14:15:09 2020
Exercise 6.5: greatest common divisor 
@author: Aaron Etienne (aetienne)
"""
def gcd(a, b):
    """This will find the greatest common divisor for a and b;
    a, b are integers in this case.
    """
    if b == 0:
        return a
    return gcd(b, a % b) 

"""Test for proof- good to test one that isn't divisible""" 
print(gcd(4, 2))
print(gcd(16, 9))