# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 09:45:32 2024

@author: Seanp
"""

def evodd (): #defining a custom function
    while True: 
        num = input("Please enter a number: ") #asks for the number
        if num.isdigit(): #makes sure the input is an ACTUAL number
            break #the loop will break if condition is met
        print ("Please enter a valid number.") #will print if input is not a number
    num = int(num) #converts the input into an integer value
    if (num % 2) == 0: #checks for the remainder
        print (num, "is an even number.") #will see if it is even
    else: 
        print (num, "is an odd number.") #will see if it is odd

evodd() #calls the function to print everything
