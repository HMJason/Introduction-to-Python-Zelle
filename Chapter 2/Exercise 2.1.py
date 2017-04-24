# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 19:12:03 2017

Exercise 2.1
Modify convert.py program to print an introduction.

@author: Jason
"""

def main():
    print("This program is going to take a temperature in Celsius and convert it into degrees Farenheit")
    celsius = eval(input("What is the Celsius temperature? "))
    fahrenheit = 9/5 * celsius + 32
    print("The temperature is", fahrenheit, "degrees Fahrenheit.")

main()

