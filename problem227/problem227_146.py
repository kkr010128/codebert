n, k = map(int, input().split())
h = list(map(int, input().split()))
h = sorted(h)
ans = 0
for i in range(max(0, n-k)):
    ans += h[i]

print(str(ans))
