#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 15:06:08 2020

@author: aetienne
"""

import math

def mysqrt(a):
    """Calculates square root utilizing netwonian method: 
        https://pages.mtu.edu/~shene/COURSES/cs201/NOTES/chap06/sqrt-1.html
    
    a: positive integer < 0
    x: the estimated value, in this case our value is a/2
    """
    x = a/2
    while True:
        est_root = (x + a/x) / 2
        if est_root == x:
            return est_root
            break
        x = est_root

def test_sqrt(list_for_a):
    """This will display the result of calculating sqrt using other various
    methods:
    list_for_a - lists a positive digit.
    """
    line1a = "a"
    line1b = "mysqrt(a)"
    line1c = "math.sqrt(a)"
    line1d = "diff"
    
    line2a = "-"
    line2b = "---------"
    line2c = "------------"
    line2d = "----"
    
    spacing1 = " "
    spacing2 = " " * 3
    spacing3 = ""
    
    """Print above setup into a table"""
    print(line1a, spacing1, line1b, spacing2, line1c, spacing3, line1d)
    print(line2a, spacing1, line2b, spacing2, line2c, spacing3, line2d)
    
    """allocate information into columns 1-4"""
    for a in list_for_a:
        col1 = float(a)
        col2 = mysqrt(a)
        col3 = math.sqrt(a)
        col4 = abs(mysqrt(a) - math.sqrt(a))

        print(col1, "{:<14f}".format(col2), "{:<14f}".format(col3), col4)

test_sqrt(range(1,15))