n = int(input())


ans = float("-INF")
min_v = int(input())
for _ in range(n-1):
    r = int(input())
    ans = max(ans, r - min_v)
    min_v = min(min_v, r)


print(ans)
