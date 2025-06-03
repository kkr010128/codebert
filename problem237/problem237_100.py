#!/usr/bin/env python
# coding: utf-8

# In[8]:


N = int(input())
mylist = []
for _ in range(N):
    x,l = map(int, input().split())
    a = x-l
    b = x+l
    mylist.append([a,b])


# In[12]:


mylist = sorted(mylist,key=lambda x:x[1])
cnt = 1
p = mylist[0][1]
for i in range(1,N):
    if mylist[i][0] < p:
        continue
    else:
        cnt += 1
        p = mylist[i][1]
print(cnt)


# In[ ]:




