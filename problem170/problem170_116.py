n,k = map(int, input().split())
ans = 0
for i in range(k,n+2):
  a = (i-1)*i//2
  ans += n*i-2*a+1
print(ans%(10**9+7))