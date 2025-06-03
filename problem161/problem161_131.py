A, B, N = map(int, input().split())


if B < N:
    Max = int(A*(B-1)/B)
    X = int(N/B)
    fx = int(A*(B*X-1)/B) - A * int((B*X-1)/B)
    # Max = max(fx,Max)
    # for x in range(1,X):
    #     fx = int(A*x/B) - A * int(x/B)
    #     Max = max(Max,fx)
elif B == N:
    Max = int(A*(B-1)/B)
else:
    Max = int(A*N/B)
print(Max)
