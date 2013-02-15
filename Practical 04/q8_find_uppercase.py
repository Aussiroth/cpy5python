#File Name: q8_find_uppercase.py
#Author: Alvin Yan
#Date Created: 15/2/2013
#Date Modified: 15/2/2013
#Description: Finds number of uppercase in string

def find_num_uppercase(string):
    if len(string)==1:
        if ord(string[0])>=65 and ord(string[0])<=90:
            return 1
        return 0
    else:
        if ord(string[0])>=65 and ord(string[0])<=90:
            return 1+find_num_uppercase(string[1:])
        return 0+find_num_uppercase(string[1:])

string = input("Enter a string\n")
print (find_num_uppercase(string))
