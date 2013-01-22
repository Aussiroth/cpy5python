#File Name: q7_generate_payroll.py
#Author: Alvin Yan
#Date Created: 21/1/2013
#Date Modified: 21/1/2013
#Description: Generates payroll

name = input("Enter name: ")
hours = int(input("Enter number of hours worked weekly: "))
payrate = float(input("Hourly pay rate: "))
cpf = float(input("CPF contribution rate (%): "))
grosspay="{0:.2f}".format(float(hours*payrate))
cpfpay=float(cpf*float(grosspay)/100)
cpfpay="{0:.2f}".format(cpfpay)
netpay="{0:.2f}".format(float(grosspay)-float(cpfpay))
print ("Payroll statement for " + name)
print ("Number of hours worked in week: " + str(hours))
print ("Hourly pay rate" + str(payrate))
print ("Gross pay = $" + str(grosspay))
print ("CPF contribution at " + str(cpf) + "% = $" + str(cpfpay))
print ("\nNet pay = $" + str(netpay))
