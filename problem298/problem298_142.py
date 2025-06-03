N, K = map(int, input().split())
ans = 0
for h in list(map(int, input().split())):
    ans += (h >= K)
print(ans)
