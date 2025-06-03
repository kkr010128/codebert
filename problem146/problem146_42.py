import math
def modpow(a, n, p):
  if n == 0:
    return 1
  if n == 1:
    return a % p 
  elif n % 2 == 1:
    return a * modpow(a, n-1, p) % p
  else:
    return modpow(a, n//2, p) **2 % p
MOD = 1000000007
n = int(input())
#初期値が0の辞書
from collections import defaultdict
pp = defaultdict(lambda: 0) 
pm = defaultdict(lambda: 0) 
def seiki(x,y):
    tmp=math.gcd(x,y)
    return (x//tmp,y//tmp)

a0b0 = 0

for i in range(n):
  a, b = map(int, input().split())

  if a == 0 and b == 0:
    a0b0 += 1
  elif a == 0:
    pp[(0,1)] += 1

  elif b == 0:
    pm[(0,1)] += 1

  elif a*b>0:
    tmp = seiki(abs(a),abs(b))
    pp[tmp] += 1

  else:
    tmp = seiki(abs(b),abs(a))
    pm[tmp] += 1

ans = 1
for key in set(pp.keys()) | set(pm.keys()):
    pp_v=pp[key]
    pm_v=pm[key]
    ans*=(modpow(2,pm_v,MOD)+modpow(2,pp_v,MOD)-1)
    ans%=MOD

ans = (ans+a0b0-1) % MOD
print(ans)
    
  
