#File Name: q2_display_pattern.py
#Author: Alvin Yan
#Date Created: 15/2/2013
#Date Modified: 15/2/2013
#Description: Displays a pattern

def display_pattern(n):
    final=""
    for i in range (1, n+1):
        final=final+str(i)+" "
    for i in range (1, n+1):
        if i<10:
                spacing=i*2
        elif 10<=i<100:
            spacing=(i-9)*3+9*2
        elif 100<=i<1000:
            spacing=(i-99)*4+90*2+9*2
        print (" "*(len(final)-spacing), end="")
        for j in range(i, 0, -1):
            print (j, end=" ")
        print ()
            

    
n = int(input("Enter an integer: "))
display_pattern(n)
