#File Name: q06_kilograms_to_pounds.py
#Author: Alvin Yan
#Date Created: 29/1/2013
#Date Modified: 29/1/2013
#Description: Prints kilogram to pound conversion table to 10kg

print ("Kilograms Pounds")
i=1
for i in range (1, 11):
    print (str(i) + " "*(9-i//10) + str(i*2.2))
