from collections import deque
from sys import stdin
input = stdin.readline

N = int(input())
neighborlist = [None for _ in range(N+1)]
for _ in range(1, N+1):
    node, _, *L = list(map(int, input().split()))
    neighborlist[node] = L

distancelist = [-1]*(N+1)
queue = deque()
queue.append(1)
distancelist[1] = 0
while queue:
    node = queue.popleft()
    distance = distancelist[node]
    for neighbor in neighborlist[node]:
        if distancelist[neighbor] == -1:
            distancelist[neighbor] = distance + 1
            queue.append(neighbor)

for i in range(1, N+1):
    print(i, distancelist[i])
