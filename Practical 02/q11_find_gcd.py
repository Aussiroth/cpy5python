#File Name: q11_find_gcd.py
#Author: Alvin Yan
#Date Created: 29/1/2013
#Date Modified: 29/1/2013
#Description: Find the greatest common denominator of 2 numbers

num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
factor=1
i=2
while i<=num1 and i<=num2:
    if num1%i==0 and num2%i==0:
        factor=i
    i=i+1
print (factor)
