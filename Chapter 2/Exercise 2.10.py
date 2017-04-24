# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 19:12:03 2017

Exercise 2.10
Write a program to perform a unit conversion of your own choosing. Make sure that the program prints an introduction that explains what it does.
Convert inches to cm.

@author: Jason
"""

def main():
    
    print("This program will convert inches to cm.")
    
    inches = eval(input("Please enter number of inches: "))
    cm = round(inches * 2.54, 1)
    
    print(str(inches) + " inches is " + str(cm) + " centimetres.")
    
    
main()


