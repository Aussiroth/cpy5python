#File Name: q6_determine_prime.py
#Author: Alvin Yan
#Date Created: 15/2/2013
#Date Modified: 15/2/2013
#Description: Finds first 1000 primes

from math import *

def is_prime(n):
    for k in range (2, int(sqrt(n)+1)):
        if n%k==0:
            return False
    return True

i = 1
j = 2
primes = []
while True:
    derp = is_prime(j)
    if derp==True:
        primes.append(j)
        i=i+1
        if i>1000:
            break
    j=j+1
k = 0
while k<1000:
    print (primes[k], primes[k+1], primes[k+2], primes[k+3], primes[k+4], primes[k+5], primes[k+6], primes[k+7], primes[k+8], primes[k+9])
    k=k+10
