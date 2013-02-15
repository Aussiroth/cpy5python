#File Name: q7_find_largest.py
#Author: Alvin Yan
#Date Created: 15/2/2013
#Date Modified: 15/2/2013
#Description: Finds largest integer in array

def find_largest(alist):
    if len(alist)==2:
        if alist[0]>alist[1]:
            return alist[0]
        return alist[1]
    else:
        if alist[0]>alist[1]:
            alist[1]=alist[0]
        return find_largest(alist[1:])

alist=[]
no = int(input("Enter number of elements to input into list: "))
for i in range (1, no+1):
    alist.append(int(input("Enter element: ")))
    
print (find_largest(alist))
            
