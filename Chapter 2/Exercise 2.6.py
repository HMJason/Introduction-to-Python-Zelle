# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 19:12:03 2017

Exercise 2.6
Suppose you have an investment plan where you invest a certain ﬁxed amount every year. 
Modify futval.py to compute the total accumulation of your investment. 
The inputs to the program will be the amount to invest each year, the interest rate, and the number of years for the investment.

@author: Jason
"""

def main():
    
    print("This program calculates the future value")
    print("of a 10-year investment.")

    principal = eval(input("Enter the initial principal: "))
    apr = eval(input("Enter the annual interest rate: "))
    years = int(input("Enter the number of investment years: "))
    annualInvestment = eval(input("Enter the annual investment amount: "))

    for i in range(years):
        principal = (principal + annualInvestment) * (1 + apr)

    print("The value in " + str(years) + " years is:", principal)

main()