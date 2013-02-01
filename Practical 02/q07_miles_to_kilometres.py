#File Name: q07_miles_to_kilometres.py
#Author: Alvin Yan
#Date Created: 29/1/2013
#Date Modified: 29/1/2013
#Description: Prints miles to kilometers table for 1-10, 25-65 (5 interval)

import math

print ("Miles Kilometres Kilometres Miles")
for i in range (1,11):
    print (str(i) + " "*(6-len(str(i))) + str("{0:.3f}".format(1.609*i)) + " "*(11-len(str("{0:.3f}".format(1.609*i)))) + str(15+i*5) + " "*(11-len(str(15+i*5))) + str("{0:.3f}".format((15+i*5)/1.609)))
