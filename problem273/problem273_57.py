N,K = map(int,input().split())
A = list(map(int,input().split()))
B = [a%K for a in A]
cs = [0]
for b in B:
    c = (cs[-1] + b-1) % K
    cs.append(c)

from collections import deque
from collections import defaultdict
qs = defaultdict(lambda: deque())

ans = 0
for i,c in enumerate(cs):
    while qs[c] and qs[c][0] + K <= i:
        qs[c].popleft()
    ans += len(qs[c])
    qs[c].append(i)
print(ans)