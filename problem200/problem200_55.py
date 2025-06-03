#!/usr/bin/env python
# coding: utf-8

# In[9]:


A,B,M = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
mylist = []
for _ in range(M):
    mylist.append(list(map(int, input().split())))


# In[11]:


ans = min(a)+min(b)
for i in range(M):
    cost = a[mylist[i][0]-1] + b[mylist[i][1]-1] - mylist[i][2]
    if cost < ans:
        ans = cost
print(ans)


# In[ ]:




