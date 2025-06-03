n, m, X = list(map(int, input().split()))

INF = 10**9
ans = INF


A = [[] for _ in range(n)]
C = [0] * n

for i in range(n):
    c_a = list(map(int, input().split()))
    C[i], A[i] = c_a[0], c_a[1:]



for s in range(0, 1 << n):
    smart = [0] * m
    cost_sum = 0
    for i in range(n):
        if (s >> i) % 2 == 0:
            continue
        cost_sum += C[i]
        for j in range(m):
            smart[j] += A[i][j]
    ok = True
    for j in range(m):
        if smart[j] < X:
            ok = False
    if ok:
        ans = min(ans, cost_sum)

if ans == INF:
    ans = -1

print(ans)
