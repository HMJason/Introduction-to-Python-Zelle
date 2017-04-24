# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 19:12:03 2017

Exercise 2.5
Modify the futval.py program (Section 2.7) so that the number of years for the investment is also a user input.
Make sure to change the ﬁnal message to reﬂect the correct number of years.

@author: Jason
"""

def main():
    
    print("This program calculates the future value")
    print("of a 10-year investment.")

    principal = eval(input("Enter the initial principal: "))
    apr = eval(input("Enter the annual interest rate: "))
    years = int(input("Enter the number of investment years: "))

    for i in range(years):
        principal = principal * (1 + apr)

    print("The value in " + str(years) + " years is:", principal)

main()


