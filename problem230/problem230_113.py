from collections import deque

N, D, A = map(int, input().split())
mons = []
for _ in range(N):
    X, H = map(int, input().split())
    mons.append((X, (H + A - 1) // A))
mons.sort()

ans = 0
q = deque([])
tot = 0
for x, h in mons:
    while q:
        x0, h0 = next(iter(q))
        if x - 2 * D <= x0:
            break
        tot -= h0
        q.popleft()
    h = max(0, h - tot)
    ans += h
    tot += h
    q.append((x, h))
print(ans)
