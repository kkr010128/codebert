#176 A
N, X, T = list(map(int, input().split()))
if N % X == 0:
    print((int(N/X)) * T)
else:
    print((int(N/X) + 1) * T)