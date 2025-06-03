n, k = map(int, input().split())
h = sorted(map(int, input().split()))
print([0, sum(h[: n - k])][n > k])