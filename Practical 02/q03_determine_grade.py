#File Name: q03_determine_grade.py
#Author: Alvin Yan
#Date Created: 29/1/2013
#Date Modified: 29/1/2013
#Description: Returns grade of score

number = int(input("Enter score: "))
if number<0 or number > 100:
    print ("Invalid! Score must be within 0 - 100.")
else:
    if number>69 and number < 101:
        print ("A")
    elif number>59 and number<70:
        print ("B")
    elif number>54 and number<60:
        print ("C")
    elif number>49 and number<55:
        print ("D")
    elif number>44 and number<50:
        print ("E")
    elif number>34 and number<45:
        print ("S")
    else:
        print ("U")
        
