N, M, Q = map(int, input().split())
X = []
for _ in range(Q):
    a, b, c, d = map(int, input().split())
    X.append((a, b, c, d))

from itertools import combinations_with_replacement

ans = 0

for p in combinations_with_replacement(range(1, M+1), N):
    tmp = 0
    p = list(p)
    for a, b, c, d in X:
        if p[b-1] - p[a-1] == c:
            tmp += d
    
    ans = max(ans, tmp)

print(ans)