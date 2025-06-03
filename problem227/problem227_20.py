N, K = map(int, input().split())
H = list(map(int, input().split()))

h = sorted(H, reverse=True)
a = h[K:]
ans = sum(a)
print(ans)