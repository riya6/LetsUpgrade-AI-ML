#!/usr/bin/env python
# coding: utf-8

# <h4>Question 1:</h4>
# Write a program to copy the contents of one file to another using a for loop. (Don’t use built-in copy
# function)

# In[3]:


text_file = open('copy.txt','w')


word_list= []


for i in range (1, 5):
    print("Please enter data: ")
    line = input()
    word_list.append(line) 


text_file.writelines(word_list) 

text_file.close()


# <h4>Question 2:</h4>
# Write a Python program to find maximum and minimum values in the dictionary. Do not use built-in min
# and max functions.

# In[4]:


income = {'Anne' : 1111,
          'Bert' : 2222,
          'Cara' : 9999999}
print(max(income, key=income.get))
print(min(income, key=income.get))

