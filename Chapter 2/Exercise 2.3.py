# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 19:12:03 2017

Exercise 2.3
Modify convert.py program with a loop that it exeutes 5 times before quitting.

@author: Jason
"""

def main():
    
    for i in range(5):
        celsius = eval(input("What is the Celsius temperature? "))
        fahrenheit = 9/5 * celsius + 32
        print("The temperature is", fahrenheit, "degrees Fahrenheit.")

main()



