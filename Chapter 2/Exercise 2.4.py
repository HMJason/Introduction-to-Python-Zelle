# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 19:12:03 2017

Exercise 2.4
Modify convert.py program so it computes and prints a table of Celsius temperatures and 
Farenheit equivalents every 10 degrees from 0 to 100C.

@author: Jason
"""

def main():
    
    for c in range(0, 110, 10):       
        f = (9/5) * c  + 32
        print(c, f, sep ='\t\t')

main()


