#File Name: q3_find_gcd.py
#Author: Alvin Yan
#Date Created: 15/2/2013
#Date Modified: 15/2/2013
#Description: Finds GCD of 2 numbers

def gcd(m, n):
    if m%n==0:
        return n
    else:
        return gcd(n, m%n)

m = int(input("Enter the first integer: "))
n = int(input("Enter the second integer: "))
if n>m:
    derp=m
    m=n
    n=derp
print (gcd(m, n))
