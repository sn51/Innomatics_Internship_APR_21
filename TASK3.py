#!/usr/bin/env python
# coding: utf-8

# In[2]:


# POLAR COORDINATES. 
# QUESTION - CONVERT THE FOLLOWING COMPLEX Z INTO ITS POLAR COORDINATES


# In[3]:


import cmath
z = complex(input())
print(abs(z))
print(cmath.phase(z))


# In[4]:


#FIND ANGLE MBC


# In[5]:


import math
AB = int(input())
BC = int(input())
output = math.degrees(math.atan(AB/BC))
print(round(output))


# In[6]:


# print the palidrome 
# 1
# 121
# 12321
# 1234321
# using only two lines of code


# In[9]:


for i in range(1,int(input())+1):
    print(round(((10**i-1)/9)**2))


# In[10]:


# MOD DIVMOD


# In[12]:


a = int(input())
b = int(input())
print(a//b)
print(a%b)
print(divmod(a,b))


# In[13]:


# power - mod Power


# In[14]:


a = int(input())
b = int(input())
m = int(input())
print(pow(a,b))
print(pow(a,b,m))


# In[15]:


# integers comes in all sizes


# In[16]:


a = int(input())
b = int(input())
c = int(input())
d = int(input())
print(a**b+c**d)


# In[17]:


# print a palidrome
# 1
# 22
# 333
# 4444
# .....


# In[18]:


for i in range(1,int(input())):
    print(round(10**i//9)*i)


# In[ ]:




