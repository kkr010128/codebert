n, k = map(int, input().split())
h = list(map(int, input().split()))
print(sum(sorted(h)[:max(0, n - k)]))