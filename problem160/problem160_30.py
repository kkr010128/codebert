# 数列生成
from itertools import combinations
N, M, Q = map(int, input().split())
ls = []
for i in range(Q):
    ls.append([int(j) for j in input().split()])
V = [[] for i in range(N+1)]
for i in range(1, M+1):
    V[1].append([i])

for i in range(1, N):
    for v in V[i]:
        b = v[-1]
        for x in range(b, M+1):
            V[i+1].append(v + [x])
ans = 0
for x in V[-1]:
    cur = 0
    for z in ls:
        if x[z[1]-1] - x[z[0]-1] == z[2]:
            cur += z[3]
    ans = max(ans, cur)
print(ans)