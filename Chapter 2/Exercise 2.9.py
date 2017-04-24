# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 19:12:03 2017

Exercise 2.9
Write a program that converts distances measured in kilometers to miles. One kilometer is approximately 0.62 miles.

@author: Jason
"""

def main():
    
    kilometres = eval(input("Please enter distance in kilometers: "))
    miles = round(kilometres * 0.62, 1)
    
    print(str(kilometres) + " kilometres is " + str(miles) + " miles.")
    
    
main()


