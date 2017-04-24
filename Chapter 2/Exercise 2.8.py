# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 19:12:03 2017

Exercise 2.4
Write a program that converts temperatures from Fahrenheit to Celsius.

@author: Jason
"""

def main():
    
    farenheit = eval(input("Please enter Farenheit: "))
    celsius = round((farenheit - 32) / 1.8, 1)
    
    print(str(farenheit) + " degrees Farenheit is " + str(celsius) + " degrees")
    
main()


