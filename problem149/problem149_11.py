import numpy as np
N, M, X = map(int,input().split())
C = []
A = []
for i in range(N):
    c = 0
    a = []
    c, *a = map(int,input().split())
    C.append(c)
    A.append(a)
inf = float("inf")
res = inf
for bit in range(1 << N):
    Cost = 0
    Wise = [0] * M
    for i in range(N):
        if (bit >> i) & 1:# i冊目を買うときの処理
            Cost += C[i]
            for j, a in enumerate(A[i]):
                Wise[j] += a
            #else:# i冊目を買わないときの処理（今回は何もしないので省略）
    if min(Wise) >= X and Cost <= res:
        res = Cost
if res == inf:
    print("-1")
else:
    print(res)
