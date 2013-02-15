#File Name: q2_sum_series2.py
#Author: Alvin Yan
#Date Created: 15/2/2013
#Date Modified: 15/2/2013
#Description: Compute the sum of a series (i/2i+1)

def sum_series2(i):
    if i==1:
        return float(i/(2*i+1))
    else:
        return (i/(2*i+1))+sum_series2(i-1)


i = int(input("Enter a positive integer: "))
print (sum_series2(i))
