N, X, T = map(int, input().split())

A = N // X
B = N % X

if B == 0:
    print(A * T)
else:
    print((A+1)*T)