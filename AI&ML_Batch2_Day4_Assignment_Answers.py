#!/usr/bin/env python
# coding: utf-8

# <h4>Question 1 :</h4>
# Research on whether addition, subtraction, multiplication, division, floor division, and modulo operations be performed on complex numbers. Based on your study, implement a Python program to demonstrate these operations.

# In[12]:


Add=(2+4j)+(3+5j)
Sub=(2+4j)-(3+5j)
Mul=(2+4j)*(3+5j)
Div=(2+4j)/(3+5j)
print("Addition of two complex numbers:",Add)
print("Subtraction of two complex numbers:",Sub)
print("Multiplication of two complex numbers:",Mul)
print("Division of two complex numbers:",Div)


# \* Floor Division and modulus operators (// and % respectively) are not allowed to be used on complex number in Python 3. \*

# <h4>Question 2:</h4>
# Research on range() functions and its parameters. Create a markdown cell and write in your own words(no copy-paste from google please) what you understand about it. Implement a small program of your choice on the same.

# * Range function is used to generate list of numbers within a given range. The range function in python only works with integers or whole numbers. Arguments passed in the range function cannot be any other data type other than an integer data type. All three arguments passed can be either positive or negative integers.The range function in python is also one of the data types.

# In[ ]:


range(100) # manages [0,1,2,3.......,99] in memory


# * Much easier than typing out each number individually. 

# In[ ]:


lst = [0,1,2,3,4,5,6,7,8,9..............................,99]


# * Parameters of range() function.
# 
# Several different implementations we can use to generate different ranges of numbers
# 
# *range (stop)
# 
# *range (start, stop)
# 
# *range (start, stop, step)

# start = the first number in the list.
# 
# stop = the last value +1.
# 
# step = the distance between each two consecutive values.
# 

# In[15]:


print("Python range()")
print("Get numbers from range 0 to 6")
for i in range(6):
    print(i, end= ', ')


# here, 
# 
#        0            1
#         
# range(start, stop, step)

# <h4>Question 3:</h4>
# Consider two numbers. Perform their subtraction and if the result of subtraction is greater than 25, print their multiplication result else print their division result.

# In[19]:


x=45
y=5

if x-y>25:
    print("mul is:", x*y)
else:
    print("div is:", x/y)


# <h4>Question 4:</h4>
# Consider a list of 10 elements of integer values. If the number in the list is divisible by 2, print the result as "square of that number minus 2".

# In[5]:


import numpy as np
List = [10,20,30,40,50,60,70,80,90,100]
num = 2
new_List  = np.divide(List, num)
print(new_List*2-2)


# <h4>Question 5:</h4>
# Consider a list of 10 elements. Print all the elements in the list which are greater than 7 when that number
# is divided 2.

# In[24]:


test_list = [1, 7, 5, 60, 3, 80,9,14,28] 
k = 7 
print ("The list : " + str(test_list))  
count = 0
for i in test_list : 
    if i/2 > k : 
        count = count + 1
print ("The numbers greater than 7 : " + str(count)) 

