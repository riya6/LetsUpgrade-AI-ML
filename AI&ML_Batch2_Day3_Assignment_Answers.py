#!/usr/bin/env python
# coding: utf-8

# #Write a program to subtract two complex numbers in Python.

# In[2]:


a= 2+7j
b= 2+1j
c=a+b
print("Addition of two complex no. is",c)


#  #Write a program to find the fourth root of a number.

# In[3]:


3**4


# #Write a program to swap two numbers in Python with the help of a temporary variable.

# In[7]:


z=6
y=8
temp=z
z=y
y=temp
print("Value of z:",z)
print("Value of y:",y)


# #Write a program to swap two numbers in Python without using a temporary variable.

# In[11]:


x=8
y=2
x=x^y
y=x^y
x=x^y
print("Value of x:",x)
print("Value of y:",y)


# #Write a program to convert Fahrenheit to kelvin and celsius both.

# In[3]:


def to_cel(x):
    cel=(x-32)*5/9
    print('celis:',cel)
def to_kel(x):
    cel=(x-32)*5/9+273.15
    print('kel is:',cel)
x=55
to_cel(x)
to_kel(x)
       


# #Write a program to demonstrate all the available data types in Python. Hint: Use type() function.

# In[24]:


a = 8
print(type(a)) 
  
b = 6.60
print(type(b)) 
  
c = 4 + 8j
print(type(c)) 

St=("Data Science")
print(type(St))

Lst=([0,1,'data',0,1])
print(type(Lst))

Tup=(('Data Science',0,'AI',1,'ML'))
print(type(Tup))

Bl1=True
Bl2=False
print(type(Bl1))
print(type(Bl2))

D = {1:'AI',2: 'ML',3: 'DL'} 
print(type(D))

S = {'AI', 'ML', 'DL'} 
print(type(S))

