from collections import deque

n, u, v = map(int, input().split())
edge = [[] for _ in range(n)]
for _ in range(n-1):
    a, b = map(int, input().split())
    edge[a-1].append(b-1)
    edge[b-1].append(a-1)

d_1 = deque()
d_1.append(u-1)
dist_1 = [-1] * n
dist_1[u-1] = 0
while d_1:
    node = d_1.popleft()
    for next_node in edge[node]:
        if dist_1[next_node] < 0:
            dist_1[next_node] = dist_1[node] + 1
            d_1.append(next_node)

d_2 = deque()
d_2.append(v-1)
dist_2 = [-1] * n
dist_2[v-1] = 0
while d_2:
    node = d_2.popleft()
    for next_node in edge[node]:
        if dist_2[next_node] < 0:
            dist_2[next_node] = dist_2[node] + 1
            d_2.append(next_node)

res = 0
for i in range(n):
    if dist_1[i] < dist_2[i]:
        res = max(res, dist_2[i]-1)
print(res)