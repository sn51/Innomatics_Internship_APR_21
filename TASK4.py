#!/usr/bin/env python
# coding: utf-8

# In[1]:


#sWaP cASE


# In[2]:


def swap_case(s):
    return s.swapcase()

s = input()
result = swap_case(s)
print(result)


# In[3]:


# string split and join


# In[4]:


def split_and_join(line):
    line = line.split(" ")
    line = "-".join(line)
    return(line)
line = input()
result = split_and_join(line)
print(result)


# In[5]:


# What's your name?


# In[6]:


def print_full_name(first,last):
    print("Hello",first,last+'!','You just delved into python.')
first_name = input()
last_name = input()
print_full_name(first_name,last_name)


# In[7]:


# mutations


# In[9]:


def mutate_string(string,position,character):
    string = string[:position] + character + string[position+1:]
    
    return string

s = input()
i,c = input().split()
s_new = mutate_string(s, int(i),c)
print(s_new)


# In[1]:


# string formatting


# In[2]:


def print_formatted(number):
    # your code goes here
    for i in range(1,number+1):
        binarylength = len(str(bin(number)))
        octal = oct(i).split('o')
        hexa = hex(i).split('x')
        bina = bin(i).split('b')
        print(i,octal[1],hexa[1].upper(),bina[1])

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)


# In[3]:


# albhabet rangoli


# In[4]:


def print_rangoli(size):
    # your code goes here
    import string
    alpha = string.ascii_lowercase

    list1 = []
    for i in range(n):
        l = "-".join(alpha[i:n])
        list1.append((l[::-1]+l[1:]).center(4*n-3, "-"))
        
    print('\n'.join(list1[:0:-1]+list1))

    
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)


# In[5]:


# capitalize


# In[11]:


import math
import os
import random
import re
import sys

def solve(s):
    for i in s.split():
        s = s.replace(i,i.capitalize())
    return s


s = input()

result = solve(s)
print(result)



# In[12]:


# door mat design


# In[13]:


M,N = map(int,input().split())
for counter in range(1,M,2):
    print((counter*".|.").center(N,"-"))
print("WELCOME".center(N,"-"))
for counter in range(M-2,-1,-2):
    print((counter*".|.").center(N,"-"))


# In[14]:


# THE MINION GAME


# In[15]:


def minion_game(string):
    # your code goes here
    FIRST_PLAYER = 0;
    SECOND_PLAYER = 0;
    len_of_str = len(string)
    for i in range(len_of_str):
        if s[i] in "AEIOU":
            FIRST_PLAYER += (len_of_str)-i
        else:
            SECOND_PLAYER += (len_of_str)-i
    if FIRST_PLAYER > SECOND_PLAYER:
        print("Kelvin",FIRST_PLAYER)
    elif( FIRST_PLAYER < SECOND_PLAYER):
        print("Stuart",SECOND_PLAYER)
    
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)


# In[16]:


# merge the tools


# In[17]:


from collections import OrderedDict
def merge_the_tools(string, k):
    # your code goes here
    l = len(string)
    for i in range(0,l,k):
        print(''.join(OrderedDict.fromkeys(string[i:i+k])))
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)


# In[ ]:




