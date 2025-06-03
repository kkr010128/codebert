import sys

input = sys.stdin.buffer.readline
r, c, k = map(int, input().split())


graph = [[0] * (c) for _ in range(r)]

for _ in range(k):
    d, e, f = map(int, input().split())
    graph[d - 1][e - 1] = f


infi = 10 ** 10
money = [[[-infi] * (c) for _ in range(r)] for _ in range(4)]
money[0][0][0] = 0
for i in range(r):
    for j in range(c):
        for t in range(4):
            m = money[t][i][j]
            delta = graph[i][j]
            if i < r - 1:
                ni = i + 1
                nj = j
                nt = 0
                money[nt][ni][nj] = max(money[nt][ni][nj], m)
                if t < 3:
                    money[nt][ni][nj] = max(money[nt][ni][nj], m + delta)

            if j < c - 1:
                ni = i
                nj = j + 1
                nt = t
                money[nt][ni][nj] = max(money[nt][ni][nj], m)
                if t < 3:
                    nt = t + 1
                    money[nt][ni][nj] = max(money[nt][ni][nj], m + delta)

ans = 0
if graph[r - 1][c - 1] > 0:
    for t in range(3):
        money[t][r - 1][c - 1] += graph[r - 1][c - 1]
for i in range(4):
    ans = max(money[i][r - 1][c - 1], ans)

print(ans)
