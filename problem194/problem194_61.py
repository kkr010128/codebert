#!/usr/bin/env python
# coding: utf-8

# In[7]:


H,W = map(int, input().split())
s_mat = []
for _ in range(H):
    s_mat.append(input())


# In[32]:


dp = [[1000 for i in range(W+1)] for j in range(H+1)]
dp[0][1] = 0
dp[1][0] = 1

for h in range(H):
    for w in range(W):
        dp[h+1][w+1] = min(
            dp[h][w+1] + (s_mat[h][w] == "#" and (h==0 or s_mat[h-1][w] == ".")),
            dp[h+1][w] + (s_mat[h][w] == "#" and (w==0 or s_mat[h][w-1] == "."))
        )
        
print(dp[-1][-1])


# In[ ]:




