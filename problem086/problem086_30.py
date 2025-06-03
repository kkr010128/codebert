# 入力
N, X, T = input().split()

N = int(N)
X = int(X)
T = int(T)

if N % X == 0:
    cnt = int(N / X)
else:
    cnt = int(N / X + 1)

print(cnt * T)