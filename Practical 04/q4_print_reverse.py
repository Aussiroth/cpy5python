#File Name: q4_print_reverse.py
#Author: Alvin Yan
#Date Created: 15/2/2013
#Date Modified: 15/2/2013
#Description: Prints number in reverse

def reverse_int(n):
    if n<10:
        print (n)
    else:
        print (n%10, end="")
        reverse_int(n//10)

n = int(input("Enter an integer: "))
reverse_int(n)
