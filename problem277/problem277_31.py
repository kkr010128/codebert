import sys
input = sys.stdin.readline
from bisect import *

H, W, K = map(int, input().split())
S = [input()[:-1] for _ in range(H)]
ans = [[-1]*W for _ in range(H)]
now = 1
l = []

for i in range(H):
    cnt = 0
    
    for j in range(W):
        if S[i][j]=='#':
            cnt += 1
    
    if cnt==0:
        continue
    
    l.append(i)
    c = 0
    
    for j in range(W):
        ans[i][j] = now
        
        if S[i][j]=='#':
            c += 1
            
            if c<cnt:
                now += 1
    
    now += 1
    
for i in range(H):
    if '#' not in S[i]:
        j = bisect_left(l, i)
        
        if j==len(l):
            for k in range(W):
                ans[i][k] = ans[l[-1]][k]
        else:
            for k in range(W):
                ans[i][k] = ans[l[j]][k]

for ans_i in ans:
    print(*ans_i)