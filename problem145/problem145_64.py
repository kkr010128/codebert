#D
from collections import deque
n, m = map(int, input().split())
ans = [0] * (n+1)
g = [[] for _ in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)
#BPS幅優先探索を行う -> 前の座標を記入
nque = deque([1])
while nque:
    now_cave = nque.popleft()
    for next_cave in g[now_cave]:
        if ans[next_cave] == 0:
            ans[next_cave] = now_cave
            nque.append(next_cave)
#         print(nque)
# print(ans)
print("Yes")
for i in range(2, n + 1):
    print(ans[i])
