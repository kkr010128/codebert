n, k, s = map(int, input().split())
ans = [s]*k
if s != 1: ans += [s-1]*(n-k)
else: ans += [2]*(n-k)
print(*ans)