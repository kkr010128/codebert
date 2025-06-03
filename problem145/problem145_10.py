from collections import deque

n, m = map(int, input().split())

# dist = [-1 for i in range(n)]
prenodes = [-1 for i in range(n)]

G = [[] for i in range(n)]
ab = []
for i in range(m):
    ab.append(list(map(int, input().split())))

for i in range(m):
    G[ab[i][0]-1].append(ab[i][1]-1)
    G[ab[i][1]-1].append(ab[i][0]-1)
# print(G)

# dist[0] = 0
prenodes[0] = 0
que = deque([0])

while len(que) != 0:
    v = que.popleft()

    for vi in G[v]:
        if prenodes[vi] != -1:
            continue
        que.append(vi)
        # dist[vi] = dist[v] + 1
        prenodes[vi] = v

ans = "Yes"
for i in range(n):
    if prenodes[i] == -1:
        ans = "No"
        break

if ans == "No":
    print(ans)
else:
    print(ans)
    for i in range(1, n):
        print(prenodes[i]+1)
