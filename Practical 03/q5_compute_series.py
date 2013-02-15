#File Name: q5_compute_series.py
#Author: Alvin Yan
#Date Created: 15/2/2013
#Date Modified: 15/2/2013
#Description: Computes a series

def series(i):
    print ("i", "m(i)")
    sum=0.0
    k=1
    while k<=i:
        sum=sum+float(1/(2*k-1))
        sum=sum-float(1/(2*k+1))
        print (k, "{0:.12f}".format(sum*4.0))
        k=k+2


i = int(input("Enter an odd integer: "))
series(i)
