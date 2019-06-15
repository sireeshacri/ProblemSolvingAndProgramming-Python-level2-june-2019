#!/usr/bin/env python
# coding: utf-8

# # Problem Solving and Programming 
# 
# #### Date 12 June 2019
# 
# #### Day Objectives
# 
# - String Slicing
# - Functions in Python
# - Basic Problems related to conditional statements using functions
# - Iteration in Python
# - Python Data Structures - Lists, Tuples and Dictionaries
# - Basic Operations on data structures
#     - Applying Data Structures to solve problems

# In[ ]:





# ## String Slicing

# In[28]:


s1 = 'Python'

s1[0] # Accessing the first charcter in a string

s1[1] #Accessing the second character in a string

s1[len(s1)-1]  #Accessing the last charcater in a string

s1[-1]  # Another way of accessing the last character 

s1[-2]  # Accessing the penultimate (from last the second one) character of a string

s1[0:2] # Accessing last two characters in this '0' is inclusive(that is first part) and '2' is exclusive(second character)

s1[-2:]  #Accessing the last two charcters in a string in any string length
 
s1[:-2]  #Accessing the whole string excluding the last two characters

s1[4:]  #Accessing the last two character if the above string length  or Accessing all characters 5th character to end of string

# Accessing all character except first and last character

s1[1:-1]

s1[1:] #Accessing all characters except the first one

# Accessing the middle character in odd length a string

s1[len(s1)//2]


# In[ ]:




