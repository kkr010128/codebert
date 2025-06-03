from collections import deque

N, X, Y = [int(x) for x in input().split()]
X -= 1
Y -= 1

result = {x: 0 for x in range(N)}


def push(v, d, queue, dist):
    if v in dist:
        return
    dist[v] = d
    queue.appendleft(v)


def check(i):
    queue = deque()
    dist = {}
    push(i, 0, queue, dist)

    while queue:
        pos = queue.pop()
        d = dist[pos]

        if pos - 1 >= 0:
            push(pos - 1, d + 1, queue, dist)
        if pos + 1 < N:
            push(pos + 1, d + 1, queue, dist)
        if pos == X:
            push(Y, d + 1, queue, dist)
        if pos == Y:
            push(X, d + 1, queue, dist)

    for i in range(N):
        result[dist[i]] += 1


for i in range(N):
    check(i)

for i in range(1, N):
    print(result[i] // 2)
