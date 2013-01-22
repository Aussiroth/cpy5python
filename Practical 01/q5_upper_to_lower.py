#File Name: q5_upper_to_lower.py
#Author: Alvin Yan
#Date Created: 21/1/2013
#Date Modified: 21/1/2013
#Description: Change uppercase to lowercase character by ASCII value

word=input("Please input a character\n")
for a in word:
    print (chr(ord(a)+32))
