n, k = map(int, input().split())
data = list(map(int, input().split()))
ans = 0
for d in data:
    if d >= k:
        ans += 1

print(ans)
