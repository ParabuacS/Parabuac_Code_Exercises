# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 12:22:27 2024

@author: Seanp
"""

#code below is dictionary for months in the year with respective number of days
year = {
        "1" : 31,
        "2" : 28,
        "3" : 31,
        "4" : 30,
        "5" : 31,
        "6" : 30,
        "7" : 31,
        "8" : 31,
        "9" : 30,
        "10" : 31,
        "11" : 30,
        "12" : 31,
        }

while True: 
    month = int(input("Input the month number: "))
    if month >=1 and month <=12: #making sure the month numbers are valid
        break #loop breaks if condition is met
    print ("Please enter a valid month number.")#otherwise this will loop print


leap = input("Is it a leap year? ")#asking for leap year
leap2 = "yes"
leap3 = "no"
if leap.casefold() == leap2.casefold() : 
    if month == 2:
        print ("Days in February: 29")#answer if february in leap year
elif leap.casefold() == leap3.casefold():
    if month == 2: 
        print (f"Days in February: {year['2']}")#answer if february in normal year
elif leap.casefold() != leap2.casefold() or leap.casefold() != leap3.casefold():
    print ("Please answer with yes or no.")#will print if 'yes' and 'no' aren't the inputs

"""
code below is used to declare the number of days
in each month as given by the user
codes above will make sure that the input number is validated (must be 1-12)
and dependent on leap year for february (2)
"""

if month == 1:
    print (f"Days in January: {year['1']}")
elif month == 3:
    print (f"Days in March: {year['3']}")
elif month == 4:
    print (f"Days in April: {year['4']}")
elif month == 5:
    print (f"Days in May: {year['5']}")
elif month == 6:
    print (f"Days in June: {year['6']}")
elif month == 7:
    print (f"Days in July: {year['7']}")
elif month == 8:
    print (f"Days in August: {year['8']}")
elif month == 9:
    print (f"Days in September: {year['9']}")
elif month == 10:
    print (f"Days in October: {year['10']}")
elif month == 11:
    print (f"Days in November: {year['11']}")
elif month == 12:
    print (f"Days in December: {year['12']}")
    