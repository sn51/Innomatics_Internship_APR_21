#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# SAY "Hello, World!" WITH PYTHON


# In[2]:


print("Hello, World!")


# In[4]:


# Given an integer, , perform the following conditional actions:

#If n is odd, print Weird
#If n is even and in the inclusive range of 2 to 5, print Not Weird
#If n is even and in the inclusive range of 6 to 20, print Weird
#If n is even and greater than 20 , print Not Weird


# In[5]:


n = int(input())

if (n%2 == 0 and 2<=n<=5):
    print('Not Weird')
elif(n%2==0 and 6<=n<=20):
    print('Weird')
elif(n%2==0 and 21<=n<=100):
    print('Not Weird')
else:
    print('Weird')


# In[6]:


#The provided code stub reads two integers from STDIN, a and b. Add code to print three lines where:

#The first line contains the sum of the two numbers.
#The second line contains the difference of the two numbers (first - second).
#The third line contains the product of the two numbers.


# In[7]:


a = int(input())
b = int(input())

print(a+b)
print(a-b)
print(a*b)


# In[8]:


#the provided code stub reads two integers, a and b, from STDIN.

#Add logic to print two lines. The first line should contain the result of integer division, a //b . 
#The second line should contain the result of float division, a /b .

#No rounding or formatting is necessary.


# In[9]:


a = int(input())
b = int(input())

print(a//b)
print(a/b)


# In[10]:


#The provided code stub reads and integer,n , from STDIN. For all non-negative integers i<n , print i^2 .


# In[11]:


n = int(input())

for i in range(1,n):
    print(i**2)


# In[13]:


#An extra day is added to the calendar almost every four years as February 29, and the day is called a leap day.
#It corrects the calendar for the fact that our planet takes approximately 365.25 days to orbit the sun. 
#A leap year contains a leap day.

#In the Gregorian calendar, three conditions are used to identify leap years:

#The year can be evenly divided by 4, is a leap year, unless:
#The year can be evenly divided by 100, it is NOT a leap year, unless:
#The year is also evenly divisible by 400. Then it is a leap year.


# In[14]:


def is_leap(year):
    leap = False
    
    # Write your logic here
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        leap = True
    
    return leap

year = int(input())
print(is_leap(year))
    


# In[15]:


# print 123....


# In[17]:


n = int(input())

print(*range(1,n+1),sep='')


# In[ ]:




