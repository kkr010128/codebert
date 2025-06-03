import sys


def dfs(u):
    global time
    color[u] = "GRAY"
    time += 1
    d[u] = time
    for v in range(n):
        if M[u][v] and color[v] == "WHITE":
            dfs(v)
    color[u] = "BLACK"
    time += 1
    f[u] = time


if __name__ == "__main__":
    n = int(sys.stdin.readline())
    color = ["WHITE"] * n
    time = 0
    d = [-1] * n
    f = [-1] * n
    M = [[0] * n for i in range(n)]
    for inp in sys.stdin.readlines():
        inp = list(map(int, inp.split()))
        for i in inp[2:]:
            M[inp[0]-1][i-1] = 1
    for i in range(n):
        if d[i] == -1:
            dfs(i)
    for i in range(n):
        print(i+1, d[i], f[i])