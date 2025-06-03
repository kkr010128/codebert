N,M = map(int,input().split())
f = [[] for i in range(N)]
for i in range(M):
    A,B = map(int,input().split())
    f[A-1].append(B-1)
    f[B-1].append(A-1)
from collections import deque
d = deque()
x = [-1]*N
for i in range(N):
    if x[i] == -1:
        x[i] = i
        d.append(f[i])
    while len(d) > 0:
        z = d.popleft()
        for j in z:
            if x[j] == -1:
                x[j] = i
                d.append(f[j])
import collections
ans = collections.Counter(x)
print(ans.most_common()[0][1])