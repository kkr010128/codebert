from copy import copy
import random
D = int(input())
c = list(map(int,input().split()))
s = [list(map(int,input().split())) for _ in range(D)]
last = [0]*26
ans = [0]*D
score = 0
for i in range(D):
    ps = [0]*26
    for j in range(26):
        pl = copy(last)
        pl[j] = i+1
        ps[j] += s[i][j]
        for k in range(26):
            ps[j] -= c[k]*(i+1-pl[k])
    idx = ps.index(max(ps))
    last[idx] = i+1
    ans[i] = idx+1
    score += max(ps)
for i in range(40000):
    na = copy(ans)
    x = random.randint(1,365)
    y = random.randint(1,365)
    if x == y:
        continue
    na[x-1],na[y-1] = na[y-1],na[x-1]
    last = [0]*26
    ns = 0
    for i in range(D):
        last[na[i]-1] = i+1
        ns += s[i][na[i]-1]
        for j in range(26):
            ns -= c[j]*(i+1-last[j])
    if ns > score:
        ans = na
        score = ns
for a in ans:
    print(a)