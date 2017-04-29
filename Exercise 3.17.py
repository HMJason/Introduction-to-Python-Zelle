# -*- coding: utf-8 -*-
"""
Created on Sat Apr 29 19:14:41 2017

Exercise 3.17
You have seen that the math library contains a function that computes the square root of numbers. 
In this exercise, you are to write your own algorithm for computing square roots. One way to solve this problem is to use a guess-and-check approach. 
You ﬁrst guess what the square root might be and then see how close your guess is. 
You can use this information to make another guess and continue guessing until you have found the square root (or a close approximation to it). 
One particularly good way of making guesses is to use Newton’s method. Suppose x is the number we want the root of and guess is the current guessed answer. 
The guess can be improved by using guess+guess as the next guess.
Write a program that implements Newton’s method. The program should prompt the user for the value to ﬁnd the square root of (x) and the 
number of times to improve the guess. Starting with a guess value of x/2, your program should loop the speciﬁed number of times applying Newton’s method 
and report the ﬁnal value of guess. You should also subtract your estimate from the value of math.sqrt(x) to show how close it is.

@author: Jason
"""

def main():
    
    import math
    
    root = float(input("Please enter the number we want the root of: "))
    
    if root <= 0.0:
        print("Please enter a positive real number.")
    else:
        maxIterations = int(input("How many iterations do you want: "))
        benchmark = math.sqrt(root)
        
        x0 = root/2
        f_x = x0**2 - root
        derivative_f_x = 2 * root
        for i in range(maxIterations):            
            x = x0 - (f_x) / derivative_f_x       
            x0 = x
            f_x = x**2 - root
            derivative_f_x = 2 * x     
        print("The root of " + str(root) + " is " + str(x))
        print("The absolute error in the esimate is " + str(abs(x - benchmark)))
        
main()

