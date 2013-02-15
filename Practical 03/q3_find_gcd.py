#File Name: q3_find_gcd.py
#Author: Alvin Yan
#Date Created: 15/2/2013
#Date Modified: 15/2/2013
#Description: Finds GCD of 2 numbers

def gcd (m, n):
    i = 1
    while i<n and i<m:
        if m%i==0 and n%i==0:
            max=i
        i=i+1
    print (i)

m = int(input("Enter the first integer: "))
n = int(input("Enter the second integer: "))
gcd (m, n)
