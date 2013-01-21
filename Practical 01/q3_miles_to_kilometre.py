#File Name: q3_miles_to_kilometre
#Author: Alvin Yan
#Date Created: 21/3/2013
#Date Modified: 21/1/2013
#Description: Converts miles to kilometers

miles = float(input("Input the number of miles"))
area2=float(miles/1.60934)
area="{0:<10.3f}".format(area2)
print (area)
