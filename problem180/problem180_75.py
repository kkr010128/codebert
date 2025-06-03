N, K = list(map(int, input().split()))
if abs(N - K) > N:
    print(N)
else:
    if N % K == 0:
        N = 0
    else:
        N = abs(N % K - K)
    print(N)