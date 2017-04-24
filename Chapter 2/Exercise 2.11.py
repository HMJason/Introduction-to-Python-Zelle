# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 19:12:03 2017

Exercise 2.11
Write an interactive Python calculator program. The program should allow the user to type a mathematical expression, 
and then print the value of the expression. Include a loop so that the user can perform many calculations (say, up to 100). 
Note: to quit early, the user can make the program crash by typing a bad expression or simply closing the window that the calculator program is running in. 
You’ll learn better ways of terminating interactive programs in later chapters.
@author: Jason
"""

def main():
    
    for i in range(100):
        expression = eval(input("Please enter an expression: "))
        print("The answer is " + str(expression))
        
main()


