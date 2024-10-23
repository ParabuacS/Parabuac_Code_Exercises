# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 18:10:37 2024

@author: Seanp
"""

password = "Seen1Aika69" #the correct password with case-sesitivity

attempts = 0 #number of starting attempts
max_attempts = 5 #max number of attempts

while attempts < max_attempts:
    use_pw = input("Please enter the password: ")#asking for input
    if use_pw == password:
        print ("Password accepted, access granted.")#print if password is correct
        break
    else:
        print ("Access denied, please try again.")#print if password is wrong
        attempts += 1
if attempts == max_attempts:
    print ("Access blocked, alerting security.")#print if max number of attempts is used