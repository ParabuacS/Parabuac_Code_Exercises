# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 10:34:39 2024

@author: Seanp
"""

Names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"] #The given list as per the exercise

for alpha in Names: #searching for Sam with a for loop
    print(alpha)
    if alpha == "Sam":
        print ("We found her!")
        break

print (Names[4]) #searching for Sam with positive indexing
print (Names[-2]) #searching for Sam with negative indexing