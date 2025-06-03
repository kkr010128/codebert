N = int(input())
mod = 1000000007
def powmod(x,y):
  res = 1
  for i in range(y):
    res = res*x%mod
  return res
ans = powmod(10,N)-powmod(9,N)-powmod(9,N)+powmod(8,N)
ans = ans%mod
ans = (ans + mod)%mod
print(ans)