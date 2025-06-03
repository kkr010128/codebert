D = int(input())
C = list(map(int, input().split()))
S = [list(map(int, input().split())) for _ in range(D)]
T = [int(input()) for _ in range(D)]
v = 0
last = [0] * 26
for d in range(D):
    # ct:current type
    ct= T[d] - 1
    last[ct] = d + 1
    # 今回の満足度
    v += S[d][ct]
    # 不満度を引く
    v -= sum([C[t] * (d + 1 - last[t]) for t in range(26)])
    print(v)