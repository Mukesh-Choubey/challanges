# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 14:28:13 2020

@author: mchoubey
"""
##1 Create 2 variables. Swap them and print their values. 

x, y = 10, 20
x, y = y, x
print(x, y)
###2 Write an if statement that compares two numbers and prints the larger
if x < y:
    print("larger" , y)
else:
    print("larger", x)
    
##3   Write an if statement that compares two strings and prints the larger. 
 
str1 = "This is shorter"
str2 = "This looks longer"
if len(str1) > len(str2):
    print(str1)
else:
    print(str2)
##4) Write a for loop that prints the evens numbers from 1-100.     
for x in range(101):
    if x % 2 == 0:
           print(x)

###5Rewrite #4 using a while loop
j = 0
while j <= 100:
    if j % 2 == 0:
        print(j)
    j +=1        
        
##6) Write a nested loop which prints the following pattern: 

for i in range(3):
    print('***')
    for j in range(1):
        print("\n")
        

