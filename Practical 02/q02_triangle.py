#File Name: q02_triangle.py
#Author: Alvin Yan
#Date Created: 29/1/2013
#Date Modified: 29/1/2013
#Description: Checks if triangle is valid and returns perimeter if is valid

side1 = int(input("Enter side 1: "))
side2 = int(input("Enter side 2: "))
side3 = int(input("Enter side 3: "))

if side1+side2<=side3:
    print ("Invalid triangle!")
elif side1+side3<=side2:
    print ("Invalid triangle!")
elif side3+side2<=side1:
    print ("Invalid triangle!")
else:
    print ("Perimeter =", side1+side2+side3)
