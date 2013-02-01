#File Name: q05_find_month_days.py
#Author: Alvin Yan
#Date Created: 29/1/2013
#Date Modified: 29/1/2013
#Description: Returns number of days in the month of the year
month = int(input("Enter the number of the month: "))
year = int(input("Enter the number of year: "))

if month==1:
    print ("January", year, "has 31 days")
elif month==3:
    print ("March", year, "has 31 days")
elif month==4:
    print ("April", year, "has 30 days")
elif month==5:
    print ("May", year, "has 31 days")
elif month==6:
    print ("June", year, "has 30 days")
elif month==7:
    print ("July", year, "has 31 days")
elif month==8:
    print ("August", year, "has 31 days")
elif month==9:
    print ("September", year, "has 30 days")
elif month==10:
    print ("October", year, "has 31 days")
elif month==11:
    print ("November", year, "has 30 days")
elif month==12:
    print ("December", year, "has 31 days")
elif month==2:
    if year%4!=0:
        print ("February", year, "has 28 days")
    else:
        if year%400==0:
            print ("February", year, "has 29 days")
        else:
            if year%100==0:
                print ("February", year, "has 28 days")
            else:
                print ("February", year, "has 29 days")
    
