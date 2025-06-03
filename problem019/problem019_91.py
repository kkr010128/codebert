from collections import deque

n, q = map(int, input().split())
ps = [input().split() for _ in range(n)]

que = deque(ps)
time = 0

while que:

    p, rest = que.popleft()

    elapsed = min(q, int(rest))
    time += elapsed
    rest = str(int(rest) - elapsed)

    if int(rest) > 0:
        que.append([p, rest])
    else:
        print(p, time)
