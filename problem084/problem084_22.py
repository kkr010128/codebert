from collections import deque

n, m = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(m)]

t = [[] for _ in range(n+1)]

for a, b in ab:
    t[a].append(b)
    t[b].append(a)

ans = 1
frag = [True]*(n+1)
d = deque()

for i in range(1, n+1):
    if not frag[i]:
        continue
    d.append(i)
    l = []
    while d:
        num = d.popleft()
        for j in t[num]:
            if not frag[j]:
                continue
            d.append(j)
            l.append(j)
            frag[j] = False
    ans = max(ans, len(set(l)))

print(ans)