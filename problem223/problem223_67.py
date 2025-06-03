#!/usr/bin/env python
# coding: utf-8

# In[43]:


N,K = map(int, input().split())
p = list(map(int, input().split()))


# In[44]:


le = [(x+1)/2 for x in p]
e = sum(le[:K])
ans = e
for i in range(N-K):
    e -= le[i]
    e += le[i+K]
    ans = max(ans ,e)
print(ans)


# In[ ]:




