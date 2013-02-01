#File Name: q08_top2_scores.py
#Author: Alvin Yan
#Date Created: 29/1/2013
#Date Modified: 29/1/2013
#Description: Prints top 2 scores from list of scores

students = int(input("Enter how many scores you are inputting\n"))
i=0
scores=[]
names=[]
while i<students:
    scores.append(int(input("Enter score: ")))
    names.append(input("Enter name: "))
    i=i+1
first=-10000
second=-10000
i=0
person1=-1
person2=-1
while i<students:
    if scores[i]>first:
        second=first
        first=scores[i]
        person2=person1
        person1=i
    elif scores[i]>second:
        second=scores[i]
        person2=i
    i=i+1
if first!=-10000:
    print (names[person1], first)
if second!=-10000:
    print (names[person2], second)

