n, k = map(int, input().split())
ans = 0

for i in range(k, n+2):
  l = (i*(i-1))*0.5
  h = (i*(2*n-i+1))*0.5
  ans += (h-l+1)

print(int(ans) % (10**9+7))