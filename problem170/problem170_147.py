ni = lambda: int(input())
nm = lambda: map(int, input().split())
nl = lambda: list(map(int, input().split()))

n,k = nm()

MOD = 10**9+7
ans = 0

for kk in range(k,n+2):
  # print()
  aa = (n-kk+n+1)*kk//2
  bb = (0+kk-1)*kk//2
  # print(aa)
  # print(bb)
  a=aa-bb
  # print(a)
  ans+=a+1%MOD

print(ans%MOD)