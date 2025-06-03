mod = 1000000007
def ff(a, b):
  ans = 1
  while b:
    if b & 1: ans = ans * a % mod
    b >>= 1
    a = a * a % mod
  return ans
n=int(input())
print(((ff(10,n)-2*ff(9,n)+ff(8,n))%mod+mod)%mod)
