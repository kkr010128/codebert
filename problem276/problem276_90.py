#!/usr/bin/env python
# coding: utf-8

# In[15]:


N = int(input())
A = list(map(int, input().split()))


# In[17]:


total = sum(A)
ans = total
left = 0
for i in A:
    left += i
    right = total - left
    ans = min(ans, abs(left - right))
#     print(left, right, ans)
print(ans)


# In[ ]:




