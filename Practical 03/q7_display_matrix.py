#File Name: q7_display_matrix.py
#Author: Alvin Yan
#Date Created: 15/2/2013
#Date Modified: 15/2/2013
#Description: Creates a n*n matrix of 0/1

from random import *

def print_matrix(n):
    matrix = []
    for i in range (0, n*n):
        matrix.append(randint(0,1))
    for i in range (0, n):
        for j in range (0, n):
            print (randint(0,1), end=" ")
        print ("")

n = int(input("Enter a positive integer: "))
print_matrix(n)
