from collections import deque

def bfs(adj_mat, d):
    Q = deque()
    N = len(d)
    color = ["W" for n in range(N)]

    Q.append(0)
    d[0] = 0

    while len(Q) != 0:
        u = Q.popleft()

        for i in range(N):
            if adj_mat[u][i] == 1 and color[i] == "W":
                color[i] = "G"
                d[i] = d[u] + 1
                Q.append(i)

        color[u] = "B"

    for i in range(N):
        if color[i] != "B":
            d[i] = -1

def Main():
    N = int(input())

    adj_mat = [[0 for n in range(N)] for n in range(N)]
    d = [0] * N

    for n in range(N):
        u, k , *V = map(int, input().split())

        if k > 0:
            for i in V:
                adj_mat[n][i - 1] = 1

    bfs(adj_mat, d)

    for n in range(N):
        print("{} {}".format(n + 1, d[n]))
Main()
