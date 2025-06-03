n, k = map(int, input().split())
h = list(map(int, input().split()))
print(sum(hi >= k for hi in h))