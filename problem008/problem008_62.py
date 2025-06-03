import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7
idx = 1


def resolve():
    def dfs(v):
        global idx
        begin[v] = idx
        idx += 1
        for u in edge[v]:
            if begin[u] != 0:
                continue
            else:
                dfs(u)
        end[v] = idx
        idx += 1

    n = int(input())
    edge = [[] for _ in range(n)]
    for _ in range(n):
        u, k, *V = map(int, input().split())
        for v in V:
            edge[u - 1].append(v - 1)

    begin = [0] * n
    end = [0] * n
    for i in range(n):
        if begin[i] == 0:
            dfs(i)
    for i in range(n):
        print(i + 1, begin[i], end[i])


if __name__ == '__main__':
    resolve()

