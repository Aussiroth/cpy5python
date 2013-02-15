#File Name: q6_sum_digits.py
#Author: Alvin Yan
#Date Created: 15/2/2013
#Date Modified: 15/2/2013
#Description: Computes sum of digits in an integer

def sum_digits(n):
    if n<10:
        return n
    return n%10+sum_digits(n//10)

n = int(input("Enter an integer: "))
print (sum_digits(n))
