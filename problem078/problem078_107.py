n = int(input())
mod = 10**9+7

def pow(n, num):
  s = num
  for i in range(1,n):
    s = s*num%mod
  return s
print((pow(n,10) - 2*pow(n,9) + pow(n,8))%mod)
