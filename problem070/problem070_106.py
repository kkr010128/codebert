from collections import deque
from collections import defaultdict

n, m = map(int, input().split())
g = defaultdict(list)
s = set(list(range(1, n+1)))
ans = 0

for i in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

while s:
    root = s.pop()
    q = deque()
    q.append(root)
    done = set()
    done.add(root)

    while q:
        node = q.popleft()

        for adj in g[node]:
            if adj not in done:
                done.add(adj)
                q.append(adj)
                s.remove(adj)
    ans += 1

print(ans - 1)