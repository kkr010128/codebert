#!/usr/bin/env python
# coding: utf-8

# In[14]:


from collections import deque


# In[21]:


S = deque(input())
Q = int(input())
rev_cnt = 0
for _ in range(Q):
    q = input().split()
    if len(q) == 1:
        rev_cnt += 1
    else:
        if (rev_cnt+int(q[1]))%2 == 0:
            S.append(q[2])
        else:
            S.appendleft(q[2])
if rev_cnt%2 == 0:
    print("".join(S))
else:
    print("".join(list(reversed(S))))    


# In[ ]:




