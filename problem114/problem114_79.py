D = int(input())
c = list(map(int, input().split()))
S = [list(map(int, input().split())) for i in range(D)]
T = [int(input()) for i in range(D)]
SUM = 0
last = [0] * 28
for d in range(1, D + 1):
    i = T[d - 1]
    SUM += S[d - 1][i - 1]
    SU = 0
    last[i] = d
    for j in range(1, 27):
        SU += (c[j - 1] * (d - last[j]))
    SUM -= SU
    print(SUM)