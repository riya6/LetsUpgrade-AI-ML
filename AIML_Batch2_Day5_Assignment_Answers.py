#!/usr/bin/env python
# coding: utf-8

# <h4>Question 1 :</h4>
# Write a Python program to find the first 20 non-even prime natural numbers.

# In[2]:


start = 1
end = 20
  
for i in range(start,end): 
    for j in range(2,i): 
        if(i % j!==0): 
            break
    else: 
        print(i) 


# In[19]:



lower = 3
upper = 23

print("Prime numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):
 
   if num > 1:
       for i in range(2, num):
        if (num % i) == 0:
            break
           
       else:
           print(num)


# <h4>Question 2 :</h4>
# Write a Python program to implement 15 functions of string.

# In[50]:


str = "1Hello Seleni"
print(str.replace("Selei","python"))

st = "Hello Selei2"
print(' '.join(reversed(st)))

s1= "Iron"
s2= "123"
print(s1.join(s2))

text = "Wonder Woman"
print(text.split()) 

c = "Checkpoint"
print(len(c)) 

s1 = "Python"
s2 = "Python"
if(s1 == s2):
      print("Both strings are equal") 
        
txt = "HACKERS"
print(txt.lower())     


str = "this is really a string ex....wow!!!";
print ("Max character: " + max(str))

str = "this-is-really-a-string-ex....wow!!!";
print ("Min character: " + min(str))

str = "jupyter pycharm";
print(str.swapcase())

str = "Do or Die";
print(str.zfill(10))
print(str.zfill(20))
 
str = u"16572009"; 
print(str.isdecimal());

str = "Data is new oil";
print("str.center(40,'*'):", str.center(40, '*'))

str = "data is new oil";
print("str.capitalize() : ", str.capitalize())


# <h4>Question 3:</h4>
# Write a Python program to check if the given string is a Palindrome or Anagram or None of them. Display the message accordingly to the user.

# In[1]:


str= ("hello")
str= ("hello")
if(str == str[::-1]):
 print ("The string is a palindrome")
if str==str:
 print ("The string is Anagram ")
else:
 print("None of them")


# <h4>Question 4:</h4>
# Write a Python's user-defined function that removes all the additional characters from the string and
# convert it finally to lower case using built-in lower(). eg: If the string is "Dr. Darshan Ingle @AIML Trainer",
# then the output be "drdarshaningleaimltrainer".

# In[6]:


original_str = "Dr. Darshan Ingle @AIML Trainer"
characters_to_remove = ".@ "
original_str.lower()

new_str = original_str
for character in characters_to_remove:
  new_str = new_str.replace(character, "").lower()

print(new_str)

