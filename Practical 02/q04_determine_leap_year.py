#File Name: q04_determine_leap_year.py
#Author: Alvin Yan
#Date Created: 29/1/2013
#Date Modified: 29/1/2013
#Description: Determine if year is leap year

year = int(input("Enter year: "))
if year%4!=0:
    print ("Non-Leap")
else:
    if year%400==0:
        print ("Leap")
    else:
        if year%100==0:
            print ("Non-leap")
        else:
            print ("Leap")
