#!/usr/bin/env python
# coding: utf-8

# In[15]:


N = int(input())


# In[16]:


ans = 0
if N%2 != 0:
    print(ans)
else:
    i = 1
    while 1:
        tmp = (5**i)*2
        if tmp <= N:
            ans += N//tmp
            i += 1
        else:
            break
    print(ans)


# In[ ]:




