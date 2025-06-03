from collections import deque

N = int(input())

Graph = {}
Node = []
visited = [-1]*(N)

for i in range(N):
    tmp = input().split()
    if int(tmp[1]) != 0:
        Graph[i] = [int(x)-1 for x in tmp[2:]]
    else:
        Graph[i] = []

queue = deque([0])
visited[0] = 0
while queue:
    x = queue.popleft()
    for i in Graph[x]:
        if visited[i] == -1:
            visited[i] = visited[x] + 1
            queue.append(i)

for i,j in enumerate(visited, 1):
    print(i, j)
