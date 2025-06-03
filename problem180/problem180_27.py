N, K = map(int, input().split())
if N >= K:
    print(min(N - (N // K) * K, ((N + K) // K) * K - N))
else:
    print(min(N, K - N))
