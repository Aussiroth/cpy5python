#File Name: q8_convert_milliseconds.py
#Author: Alvin Yan
#Date Created: 15/2/2013
#Date Modified: 15/2/2013
#Description: Converts milliseconds to hours:minutes:seconds

def convert_ms(n):
    seconds = n//1000
    minutes = seconds//60
    seconds = seconds-minutes*60
    hours = minutes//60
    minutes = minutes-hours*60
    return (str(hours)+':'+str(minutes)+':'+str(seconds))

n = int(input("Enter a positive integer: "))
print (convert_ms(n))
