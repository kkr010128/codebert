N, K = map(int, input().split())
preans = []
for n in range(K, N+2):
    MIN = (0+n-1) * n / 2
    MAX = (N + (N-n+1)) * n / 2
    preans.append(MAX - MIN+1)
    
print(int(sum(preans)%(10**9 + 7)))