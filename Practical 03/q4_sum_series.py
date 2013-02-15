#File Name: q4_sum_series.py
#Author: Alvin Yan
#Date Created: 15/2/2013
#Date Modified: 15/2/2013
#Description: Sums a series of fractions

def m_series(i):
    sums = 0.0
    for m in range(2, i+1):
        for k in range (2, m+1):
            sums = sums+float((k-1)/k)
        print (m-1, sums)
        sums=0.0

i = int(input("Enter an integer: "))
m_series(i)
