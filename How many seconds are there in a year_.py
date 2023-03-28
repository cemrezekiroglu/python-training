#!/usr/bin/env python
# coding: utf-8

# In[3]:


print ("How many seconds are there in a year?")
year= int(input("Please type a year:"))
if (year%4) == 0:
    yearly_seconds_leap = 366*24*60*60
    print("It's a leap year and and there are", yearly_seconds_leap, "seconds")
elif (year%4) != 0:
    yearly_seconds_not_leap = 365*24*60*60
    print("It's not a leap year and there are", yearly_seconds_not_leap, "seconds")

