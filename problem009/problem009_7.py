n = int(input())
d = [-1]*(n+1)
adjacent_list = [[] for _ in range(n+1)]
for _ in range(n):
    edge = list(map(int,input().split()))
    if len(edge) >= 3:
        adjacent_list[edge[0]].extend(edge[2:])

from collections import deque

que = deque()
que.append(1)
d[1] = 0
while len(que) != 0:
    v = que.popleft()
    for nv in adjacent_list[v]:
        if d[nv] == -1:
            d[nv] = d[v] + 1
        else:
            continue
        que.append(nv)

for i,dist in enumerate(d):
    if i == 0:
        continue
    print(i,dist)
