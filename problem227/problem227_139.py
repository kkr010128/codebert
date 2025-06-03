N, K = map(int, input().split())
H = sorted(map(int, input().split()))[:max(0, N-K)]
print(sum(H))
