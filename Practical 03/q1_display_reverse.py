#File Name: q1_display_reverse.py
#Author: Alvin Yan
#Date Created: 15/2/2013
#Date Modified: 15/2/2013
#Description: Function that displays integer in reverse order

def reverse_int(n):
    i = str(n)
    print (i[::-1])



n = int(input("Enter an integer: "))
reverse_int(n);
