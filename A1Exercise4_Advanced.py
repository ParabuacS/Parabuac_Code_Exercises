# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 10:58:18 2024

@author: Seanp
"""
# Quiz on European capitals
# Below is a list of the correct answers
capitals = ["paris", "berlin", "madrid", "rome", 
            "amsterdam", "brussels", "bucharest", 
            "warsaw", "reykjavik", "copenhagen"]

score = 0

useran1 = input("What is the capital of France? ") #user puts an answer
if useran1.casefold() == capitals[0].casefold() : #casefold will ignore any capitalization
    print ("Correct!")#if spelling is correct, this will print
    score += 1 #if correct, the score will be tracked
else: 
    print ("Incorrect, the answer is Paris.")#this will print if incorrect

"""
all other codes have the same rules with respective capitals
for each country without regarding capitalization
answers must be the correct spelling to be accepted
the score will be tracked until the quiz ends
"""

useran2 = input("What is the capital of Spain? ")
if useran2.casefold() == capitals[2].casefold() :
    print ("Correct!")
    score += 1
else: 
    print ("Incorrect, the answer is Madrid.")

useran3 = input("What is the capital of Germany? ")
if useran3.casefold() == capitals[1].casefold() :
    print ("Correct!")
    score += 1
else: 
    print ("Incorrect, the answer is Berlin.")
    
useran4 = input("What is the capital of Italy? ")
if useran4.casefold() == capitals[3].casefold() :
    print ("Correct!")
    score += 1
else: 
    print ("Incorrect, the answer is Rome.")

useran5 = input("What is the capital of The Netherlands? ")
if useran5.casefold() == capitals[4].casefold() :
    print ("Correct!")
    score += 1
else: 
    print ("Incorrect, the answer is Amsterdam.")

useran6 = input("What is the capital of Belgium? ")
if useran6.casefold() == capitals[5].casefold() :
    print ("Correct!")
    score += 1
else: 
    print ("Incorrect, the answer is Brussels.")
    
useran7 = input("What is the capital of Romania? ")
if useran7.casefold() == capitals[-4].casefold() :
    print ("Correct!")
    score += 1
else: 
    print ("Incorrect, the answer is Bucharest.")

useran8 = input("What is the capital of Poland? ")
if useran8.casefold() == capitals[-3].casefold() :
    print ("Correct!")
    score += 1
else: 
    print ("Incorrect, the answer is Warsaw.")

useran9 = input("What is the capital of Denmark? ")
if useran9.casefold() == capitals[-1].casefold() :
    print ("Correct!")
    score += 1
else: 
    print ("Incorrect, the answer is Copenhagen.")

useran10 = input("What is the capital of Iceland? ")
if useran10.casefold() == capitals[-2].casefold() :
    print ("Correct!")
    score += 1
else: 
    print ("Incorrect, the answer is Reykjavik.")
    
print ("Your score is:",score) # print the overall score of the user

"""
The following code below provides
feedback depending on how well
the user did on the quiz
"""
if score == 0:
    print ("How disappointing...")
elif score >= 1 and score <= 3:
    print ("Needs improvement, learn more Geography!")
elif score >= 4 and score <= 6:
    print ("Decent knowledge, keep it up!")
elif score >= 7 and score <= 9:
    print ("Worthy of praise!")
elif score == 10:
    print ("Extremely well done!")
