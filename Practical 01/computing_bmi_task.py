#File Name: computing_bmi_task.py
#Author: Alvin Yan
#Created: 21/1/2013
#Modified: 21/1/2013
#Description: Calculates BMI

height=float(input("Input your height in m\n"))
weight=float(input("Input your weight in kg\n"))
BMI=weight/(height*height)
if BMI<18.5:
    print ("Your BMI is " + str(BMI) + ". You are at risk of nutritional deficiency diseases and osteoporosis. Eat more!")
elif BMI>=18.5 and BMI<23:
    print ("Your BMI is " + str(BMI) + ". You are healthy and at low risk! :)")
elif BMI>=23 and BMI<27.5:
    print ("Your BMI is " + str(BMI) + ". You are at moderate risk. Be mindful of your weight!")
elif BMI>=27.5:
    print ("Your BMI is " + str(BMI) + ". You are at high risk of obesity. Exercise more!")
