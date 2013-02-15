#File Name: q1_sum_series1.py
#Author: Alvin Yan
#Date Created: 15/2/2013
#Date Modified: 15/2/2013
#Description: Compute the sum of a series (1/i)

def sum_series1(i):
    if i==1:
        return 1
    else:
        return float(1/i)+sum_series1(i-1)


i = int(input("Enter a positive integer: "))
print (sum_series1(i))
