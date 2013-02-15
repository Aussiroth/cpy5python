#File Name: q5_count_letter.py
#Author: Alvin Yan
#Date Created: 15/2/2013
#Date Modified: 15/2/2013
#Description: Finds occurences of character in string

def count_letter(string, ch):
    if len(string)==1:
        return (string==ch)
    else:
        return (string[0]==ch)+count_letter(string[1:], ch)

string=input("Enter a string\n")
ch = input("Enter a character: ")
print (count_letter(string, ch))
