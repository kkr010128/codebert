import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n, m = map(int, input().split())
graph = [0] + [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

from collections import deque

def bfs(graph, queue, dist, prev):
    while queue:
        current = queue.popleft()

        for _next in graph[current]:
            if dist[_next] != -1:
                continue
            else:
                dist[_next] = dist[current] + 1
                prev[_next] = current
                queue.append(_next)

queue = deque([1])
dist = [0] + [-1] * n
prev = [0] + [-1] * n
dist[1] = 0
bfs(graph, queue, dist, prev)

if -1 in dist:
    print('No')
else:
    print('Yes')
    for v in prev[2:]:
        print(v)
