#!/usr/bin/env python
# coding: utf-8

# In[5]:


H,N = map(int, input().split())
A = []; B = []
for _ in range(N):
    a,b = map(int, input().split())
    A.append(a)
    B.append(b)


# In[12]:


a_max = max(A)
dp = [0]*(H+a_max)
for i in range(H+a_max):
    dp[i] = min(dp[i-a] + b for a,b in zip(A,B))
print(min(dp[H-1:]))


# In[ ]:




