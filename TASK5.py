#!/usr/bin/env python
# coding: utf-8

# In[1]:


# DETECT FLOATING POINT NUMBER


# In[ ]:


import re
for _ in range(int(input())):
    pattern = r'^[-+]?[0-9]*\.[0-9]+$'
    print(bool(re.match(pattern,input())))


# In[1]:


# Re.split()


# In[2]:


regex_pattern = r"[.,]+"	# Do not delete 'r'.

import re
print("\n".join(re.split(regex_pattern, input())))


# In[3]:


# group(),groups(),groupdict


# In[5]:


import re
I1 = re.search(r'([a-zA-Z0-9])\1+', input().strip())
print(I1.group(1) if I1 else -1)


# In[6]:


# Re.findall(), Re.finditr()


# In[7]:


import re
vowels = 'aeiou'
consonants = 'qwrtypsdfghjklzxcvbnm'
mat = re.findall(r'(?<=[%s])([%s]{2,})[%s]'%(consonants,vowels,consonants),input(),flags=re.I)
print('\n'.join(mat or ['-1']))


# In[8]:


#Re.start(), Re.end()


# In[9]:


import re
S = input()
k = input()
m = list(re.finditer("(?=(%s))"%k,S))
if not m:
    print(-1,1)
for i in m:
    print((i.start(1),i.end(1)-1))


# In[10]:


# validationg roman numeral


# In[11]:


thousand = 'M{0,3}'
hundred = '(C[MD]|D?C{0,3})'
ten = '(X[CL]|L?X{0,3})'
digit ='(I[VX]|V?I{0,3})'
regex_pattern = r"^" +thousand+ hundred + ten + digit +'$'	# Do not delete 'r'.

import re
print(str(bool(re.match(regex_pattern, input()))))


# In[12]:


# validating phone numbers


# In[ ]:


import re
for i in range(int(input())):
    if re.match(r'[789]\d{9}$',input()):
        print('YES')
    else:
        print('NO')


# In[ ]:




