N, X, T = (int(x) for x in input().split())
if(N % X == 0):
    print((N // X) * T)
else:
    print(((N // X) + 1) * T)