#!/usr/bin/env python
# coding: utf-8

# In[21]:


N,K = map(int, input().split())
R,S,P = map(int,input().split())
T = input()


# In[22]:


points = {}
points["r"] = P
points["s"] = R
points["p"] = S

ans = 0
mylist = []
for i in range(N):
    mylist.append(T[i])
    if i >= K:
        if T[i] == mylist[-K-1]:
            mylist[-1] = "x"
        else:
            ans += points[T[i]]
    else:
        ans += points[T[i]]
print(ans)


# In[ ]:




