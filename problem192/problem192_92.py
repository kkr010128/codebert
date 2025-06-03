#!/usr/bin/env python
# coding: utf-8

# In[35]:


import collections


# In[31]:


N = int(input())
A = list(map(int, input().split()))


# In[36]:


count = collections.Counter(A)
numsum = 0
for i in count.values():
    numsum += i*(i-1)//2

for i in A:
    print(numsum - (count[i]-1))


# In[ ]:




