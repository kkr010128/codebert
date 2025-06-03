X, Y = map(int, input().split())
MOD = 10**9+7

def mod_pow(n, m):
  res = 1
  while m > 0:
    if m & 1:
      res = (res*n)%MOD
    n = (n*n)%MOD
    m >>= 1
  return res
  
if (2*Y-X)%3 != 0 or (2*X-Y)%3 != 0 or 2*Y < X or 2*X < Y:
  print(0)
else:
  A = (2*X-Y)//3
  B = (2*Y-X)//3
  m = 1
  n = 1
  for i in range(A):
    m = (m*(A+B-i))%MOD
    n = (n*(A-i))%MOD
  inverse_n = mod_pow(n, MOD-2)
  print((m*inverse_n)%MOD)