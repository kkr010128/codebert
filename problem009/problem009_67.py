INFTY = 10 ** 10

import queue

def bfs(s):
    q = queue.Queue()
    q.put(s)
    d = [INFTY] * n
    d[s] = 0
    while not q.empty():
        u = q.get()
        for v in range(n):
            if M[u][v] == 0:
                continue
            if d[v] != INFTY:
                continue
            d[v] = d[u] + 1
            q.put(v)
    for i in range(n):
        if d[i] == INFTY:
            print(i+1, -1)
        else:
            print(i+1, d[i])

n = int(input())
M = [[0] * n for _ in range(n)]

for i in range(n):
    nums = list(map(int, input().split()))
    u = nums[0] - 1
    k = nums[1]
    for j in range(k):
        v = nums[j+2] - 1
        M[u][v] = 1

bfs(0)
