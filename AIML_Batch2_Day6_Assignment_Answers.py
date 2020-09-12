#!/usr/bin/env python
# coding: utf-8

# <h4>Question 1 :</h4>
# Assuming that we have some email addresses in the "username@companyname.com" format, please
# write a program to print the company name of a given email address. Both user names and company
# names are composed of letters only.
# Input Format:
# The first line of the input contains an email address.
# Output Format:
# Print the company name in a single line.
# Example;
# Input:
# john@google.com
# Output:
# google.
# 

# In[7]:


import re
eAdd =  input()
pattern = "(\w+)@(\w+)\.(com)"
r2 = re.match(pattern,eAdd)
print(r2.group(2))


# <h4>Question 2 :</h4>
# Write a program that accepts a comma-separated sequence of words as input and prints the words in a
# comma-separated sequence after sorting them alphabetically.
# Input Format:
# The first line of input contains words separated by the comma.
# Output Format:
# Print the sorted words separated by the comma.
# Example:
# Input:
# without,hello,bag,world
# Output:
# bag,hello,without,world

# In[9]:


items=[x for x in input().split(',')]
items.sort()
print(','.join(items))


# <h4>Question 3:</h4>
# Create your own Jupyter Notebook for Sets. Reference link:
# https://www.w3schools.com/python/python_sets.asp
# 

# A set is an unordered collection of items. Every set element is unique (no duplicates) and must be immutable (cannot be changed).

# In[3]:


tset = {"Data", "Items", "Info"}

print(tset)


# In[5]:


tset = {"Data", "Items", "Info"}

for x in tset:
  print(x)


# In[15]:


tset = {"Data", "Items", "Info"}
tdata = {"Set", "Dict", "Tuple"}

tset.add("Orgo")
tset.update(["Machine", "Device", "Operation"])
tset.remove("Operation")
tset.discard("Device")

x = tset.pop()

print(x)


print(tset)

print(len(tset))

print("Info" in tset)
print("Dic" in tdata)


# In[19]:


tset={"Machine", "Device", "Operation"}

x = tset.pop()

print(x)
print(tset)


# In[20]:


tset={"Machine", "Device", "Operation"}
tset.clear()
print(tset)


# In[22]:


s1 = {"Machine", "Device", "Operation"}
s2 = {1, 2, 3}

s3 = s1.union(s2)
print(s3)


# <h4>Question 4:</h4>
# Given a list of n-1 numbers ranging from 1 to n, your task is to find the missing number. There are no
# duplicates.
# Input Format:
# The first line contains n-1 numbers with each number separated by a space.
# Output Format:
# Print the missing number
# Example:
# Input:
# 1 2 4 6 3 7 8
# Output:
# 5
# Explanation:
# In the above list of numbers 5 is missing and hence 5 is the input

# In[27]:


def getmissingnum(A):
    n = len(A)
    total = (n + 1)*(n + 2)/2
    sum_of_A = sum(A)
    return total - sum_of_A
 
A = [1, 2, 4, 6, 3, 7, 8]
miss = getmissingnum(A)
print(miss)


# <h4>Question 5:</h4>
# With a given list L, write a program to print this list L after removing all duplicate values with original order
# reserved.
# Example:
# If the input list is
# 12 24 35 24 88 120 155 88 120 155
# Then the output should be
# 12 24 35 88 120 155
# Explanation:
# Third, the seventh and ninth element of the list L has been removed because it was already present.
# Input Format:
# In one line take the elements of the list L with each element separated by a space.
# Output Format:
# Print the elements of the modified list in one line with each element separated by a space.
# Example:
# Input:
# 12 24 35 24
# Output:
# 12 24 35

# In[28]:


def removeDuplicate( li ):
    newli=[]
    seen = set()
    for item in li:
        if item not in seen:
            seen.add( item )
            newli.append(item)
    return newli
li=[]
li= list(map(int, input ().split ()))
x = removeDuplicate(li)
for i in x:
    print(i,end=" ")

