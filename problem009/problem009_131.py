from collections import deque

n = int(input())
u = [[] for i in range(n+1)] #隣接リスト
for i in range(n):
    v = list(map(int, input().split()))
    u[v[0]] = v[1:] #v = [次数, 頂点...]

d = [-1] * (n+1)
visited = [False] * (n+1)

d[1] = 0
visited[1] = True
que = deque([1])
while len(que) > 0:
    c = que.popleft()
    for i in range(1, u[c][0]+1):
        if not visited[u[c][i]]:
            que.append(u[c][i])
            visited[u[c][i]] = True
            d[u[c][i]] = d[c] + 1

for i in range(1, n+1):
    print(i, d[i])
