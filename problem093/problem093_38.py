
N, K = map(int, input().split())
P = list(map(int, input().split()))
C = list(map(int, input().split()))


# 順列を各サイクルに分解する
used = [0] * N
ss = []
for i in range(N):
    if used[i]: continue
    cur = i
    s = []
    while used[cur] == 0:
        used[cur] = 1
        s.append(C[cur])
        cur = P[cur] - 1 # 0-index
    ss.append(s)

# 各サイクルごとに考える
res = -float("inf")
for vec in ss:
    M = len(vec)
    
    # サイクルを2周したものの累積和
    accum = [0] * (2*M+1)
    for i in range(M*2):
        accum[i+1] = accum[i] + vec[i%M]

    # amari[r] := 連続するr個の総和の最大値
    amari = [-float("inf")] * M
    for i in range(M):
        for j in range(M):
            amari[j] = max(amari[j], accum[i+j]-accum[i])

    # あまりの長さで場合分け
    for r in range(M):
        if r > K: continue
        q = (K - r) // M # ループ回数
        if r == 0 and q == 0: continue

        if accum[M] > 0:
            res = max(res, amari[r] + accum[M] * q)
        elif r > 0:
            res = max(res, amari[r])

print(res)


