# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 19:12:03 2017

Exercise 2.2
Modify avg2.py program to find the average of three exam scores.

@author: Jason
"""

def main():
    print("This program computes the average of two exam scores.")
    score = []

    for i in range(3):
        temp_score = int(input("Please enter your score: "))
        score.append(temp_score)

    average = sum(score) / len(score)

    print("The average of the scores is:", average)

main()



