import sys
input = sys.stdin.readline


n, t = map(int, input().split())

DISHES = [(0, 0)]
for _ in range(n):
    a, b = map(int, input().split())
    DISHES.append((a, b))
DISHES.sort()

DP = [[0] * (t + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    a, b = DISHES[i]
    for j in range(1, t + 1):
        if j - a < 0:
            DP[i][j] = DP[i - 1][j]
        else:
            DP[i][j] = max(DP[i - 1][j], DP[i - 1][j - a] + b)

answer = 0
for k in range(1, n + 1):
    answer = max(answer, DP[k - 1][t - 1] + DISHES[k][1])

print(answer)
