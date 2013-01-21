#File Name: q4_sum_digits.py
#Author: Alvin Yan
#Date Created: 21/3/2013
#Date Modified: 21/1/2013
#Description: Obtains sum of digits in an integer

number=int(input("Input the integer, between 0 and 1000"))
summing=0
while number>9:
    summing=summing+number%10
    number=number//10
summing=summing+number
print (summing)
