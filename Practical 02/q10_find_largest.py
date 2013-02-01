#File Name: q10_find_largest.py
#Author: Alvin Yan
#Date Created: 29/1/2013
#Date Modified: 29/1/2013
#Description: Find the largest n that n^3 is less than 12000

i=1
while True:
    if i*i*i>12000:
        print (i-1)
        break
    i=i+1
