import sys
# 整数の入力
z = list(map(int, input().split()))

N = z[0]
R = z[1]
naibu = 0
if 10 <= N:
    naibu = R
else:
    naibu = R + (100 * (10 - N))
print(naibu)