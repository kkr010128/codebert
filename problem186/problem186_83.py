k, n = map(int, input().split())
a = sorted(map(int, input().split()))
ans = a[-1]-a[0]
for i in range(1, n-1):
  path = k- a[-i] + a[-i-1] 
  ans = min(ans, path)
print(ans)