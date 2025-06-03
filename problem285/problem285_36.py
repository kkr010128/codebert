#!/usr/bin/env python
# coding: utf-8

# In[86]:


# ans = [0]*(len(S)+1)
# for i in range(len(S)):
#     count_left = 0
#     count_right = 0
#     for j in range(i):
#         if S[i-j-1] == "<":
#             count_left += 1
#         else:
#             j -= 1
#             break
#     for k in range(i,len(S)):
#         if S[k] == ">":
#             count_right += 1
#         else:
#             k -= 1
#             break
#     ans[i] = max(count_left, count_right)
# #     print(count_left, count_right)
# #     print(S[i-j-1:i], S[i:k+1])
# # print(ans)
# print(sum(ans))


# In[87]:


from collections import deque
S = input()
left = deque([0])
right = deque([0])
cnt = 0
for s in S:
    if s == '<':
        cnt += 1
    else:
        cnt = 0
    left.append(cnt)
cnt = 0
for s in S[::-1]:
    if s == '>':
        cnt += 1
    else:
        cnt = 0
    right.appendleft(cnt)
ans = 0
for l, r in zip(left, right):
    ans += max(l, r)
print(ans)


# In[ ]:




