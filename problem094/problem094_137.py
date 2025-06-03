import sys
R, C, K = list(map(int, input().split()))

d = [[[0] * (C+1) for _ in range(R+1)] for _ in range(4)]
t = [[0] * (C+1) for _ in range(R+1)]

for i in range(K):
    r,c,v = list(map(int, input().split()))
    t[r][c] = v

for i in range(R+1):
    for j in range(C+1):
        for k in range(4):
            if i!=0:
                d[0][i][j] = max(d[0][i][j], d[k][i-1][j])
                d[1][i][j] = max(d[1][i][j], d[k][i-1][j] + t[i][j])

            if j!=0:
                d[k][i][j] = max(d[k][i][j], d[k][i][j-1])
                if k != 0:
                    d[k][i][j] = max(d[k][i][j], d[k-1][i][j-1] + t[i][j])

a = 0
for i in range(4):
    a = max(a, d[i][-1][-1])
print(a)
