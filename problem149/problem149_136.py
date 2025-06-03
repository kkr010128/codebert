from itertools import product


N, M, X = map(int, input().split())
C = []
A = []
for _ in range(N):
    c, *a = map(int, input().split())
    C.append(c)
    A.append(a)

ans = float("inf")
for buys in product((0, 1), repeat=N):
    cost = 0
    achivements = [0] * M
    for i, buy in enumerate(buys):
        if not buy:
            continue
        cost += C[i]
        for j in range(M):
            achivements[j] += A[i][j]
    if all(a >= X for a in achivements):
        ans = min(ans, cost)
print(ans) if ans != float("inf") else print(-1)
