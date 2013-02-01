#File Name: q12_find_factors.py
#Author: Alvin Yan
#Date Created: 29/1/2013
#Date Modified: 29/1/2013
#Description: Finds prime factors of a number
   

number = int(input("Enter the number: "))
if number == 1:
    print (1)
else:
    z=2
    factors=[]
    while number!=1:
        if number%z==0:
            number=number/z
            factors.append(z)
        else:
            z=z+1
    print (factors)
            
