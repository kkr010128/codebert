n, k = map(int, input().split())
P = [*map(lambda x: int(x)-1, input().split())]
C = [*map(int, input().split())]

INF = 10**18
score = -INF
for st in range(n):
    lap_cn = 0
    lap_sc = 0
    nx = st
    while True:
        lap_cn += 1
        lap_sc += C[nx]
        nx = P[nx]
        if nx == st: break
    lap_sc = max(0, lap_sc)

    sum_sc = 0
    k_cn = 0
    while True:
        k_cn += 1
        if k < k_cn: break
        sum_sc += C[nx]
        score = max(score, sum_sc + lap_sc * ((k - k_cn) // lap_cn))
        nx = P[nx]
        if nx == st: break

print(score)
