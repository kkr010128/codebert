#!/usr/bin/env python
# coding: utf-8

# In[8]:


S = input()
K = int(input())


# In[10]:


cnt = 0
ans = 0
tmp = S[0]
fcnt = 0
for s in S:
    if tmp == s:
        cnt += 1
        tmp = s
    else:
        ans += cnt//2
        if fcnt == 0:
            fcnt = cnt
        cnt = 1
        tmp = s
if fcnt == 0:
    fcnt = cnt
ans += cnt//2
ans *= K

if len(S) == fcnt:
    ans = (len(S)*K)//2
elif S[0] == S[-1]:
    ans -= (fcnt//2 + cnt//2 - (fcnt+cnt)//2) * (K-1)
print(ans)


# In[ ]:




