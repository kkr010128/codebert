mod = 10**9+7
MAX_N = 10 ** 6
fact = [1]
fact_inv = [0] * (MAX_N + 4)
for i in range(MAX_N + 3):
  fact.append(fact[-1] * (i + 1) % mod)
fact_inv[-1] = pow(fact[-1], mod - 2, mod)
for i in range(MAX_N + 2, -1, -1):
  fact_inv[i] = fact_inv[i + 1] * (i + 1) % mod
def mod_comb_k(n, k, mod):
  return fact[n] * fact_inv[k] % mod * fact_inv[n - k] % mod
x,y=map(int,input().split())
if (2*x-y)>=0 and (2*y-x)>=0 and (x+y)%3==0:
  print(mod_comb_k((x+y)//3,(2*y-x)//3,mod))
else:print(0)