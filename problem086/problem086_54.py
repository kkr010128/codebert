N, X, T = map(int,input().split())
n = 0

if N % X == 0:
    n = N / X
else:
    n = N // X + 1

print(int(n * T))