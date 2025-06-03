N = int(input())
A = list(map(int, input().split()))
MOD = 10**9+7

def gcd(x, y):
  while(x % y != 0 and y % x != 0):
    if(x > y):
      x = x % y
    else:
      y = y % x
  if(x > y):
    return y
  else:
    return x
      
def lcm(x, y, MOD):
  return x * y // gcd(x, y)

X = 1
ans = 0
for i in range(N):
  X = lcm(X, A[i], MOD)
for i in range(N):
  ans = (ans + X*pow(A[i], MOD-2, MOD))%MOD
print(ans)