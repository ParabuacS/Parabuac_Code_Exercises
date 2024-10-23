# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 09:30:06 2024

@author: Seanp
"""

#name hometown and age using dictionary
alpha = {
    "name" : input("Please enter your first and last name: "), #take and store a name
    "home" : input("Please enter your hometown: "), #take and store hometown
    }
while True : 
    age = input("Please enter your age: ") #take the user's age
    if age.isdigit() : #if statement to check user input is an integer
        break #if condition is met the loop will break
    print ("Please enter a valid number.") #if condition isn't met this will print

print (f"Name: {alpha['name']}\nHome: {alpha['home']}\nAge:" ,age)#all answers will be printed
