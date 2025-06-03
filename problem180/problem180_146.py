N, K = map(int, input().split())
if N < K:
    print(min(abs(N - K), N))
else:
    div, mod = divmod(N, K)
    print(min(abs(mod-K), mod))
