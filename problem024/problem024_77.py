# -*- coding: utf-8 -*-
"""
Created on Mon Apr 30 15:18:29 2018
ALDS1-4c
@author: maezawa
"""
def can_load(w, k, p):
    n = len(w)
    m = 0
    tk = 0
    i = 0
    while tk < k:
        if m + w[i] <= p:
            m += w[i]
            i += 1
            if i >= n:
                return n+1
        else:
            m = 0
            tk += 1
    return i


n, k = list(map(int, input().split()))
w = []
tr = [0 for _ in range(k)]

for i in range(n):
    w.append(int(input()))

maxw = max(w)
# =============================================================================
# for p in range(maxw, maxw*n):
#     if can_load(w, k, p) == n:
#         print(p)
#         break
# =============================================================================
right = maxw*n
left = maxw
while left<right:
    mid = (right+left)//2
    cl = can_load(w, k, mid)
#    if cl == n:
#        print(mid)
#        break
#    elif cl < n:
    if cl < n:
        left = mid + 1
    else:
        right = mid
print(right)    
    
    
    
    
    
