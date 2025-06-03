import queue
from collections import namedtuple
T = namedtuple("T", "u d")

n = int(input())
path = dict()
ans = [-1] * (n + 1)

for i in range(n):
    a = [int(x) for x in input().split()]
    a.reverse()

    u, k = a.pop(), a.pop()
    path[u] = set()
    for j in range(k):
        path[u].add(a.pop())


def bfs(s):
    q = queue.Queue()
    q.put(s)

    while q.qsize() != 0:
        p = q.get()
        if p.d < ans[p.u] or ans[p.u] < 0:
            ans[p.u] = p.d
            for r in path[p.u]:
                q.put(T(r, p.d + 1))


bfs(T(1, 0))
for i in range(1, n + 1):
    print(i, ans[i])

