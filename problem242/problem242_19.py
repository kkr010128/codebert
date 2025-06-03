def cmb(n, r, p):
  if (r < 0) or (n < r):
    return 0
  r = min(r, n - r)
  return fact[n] * factinv[r] * factinv[n-r] % p

p = 10 ** 9 + 7
N, K = map(int,input().split())
As = list(map(int,input().split()))
As.sort()

fact = [1, 1]  # fact[n] = (n! mod p)
factinv = [1, 1]  # factinv[n] = ((n!)^(-1) mod p)
inv = [0, 1]  # factinv 計算用
 
for i in range(2, N + 1):
  fact.append((fact[-1] * i) % p)
  inv.append((-inv[p % i] * (p // i)) % p)
  factinv.append((factinv[-1] * inv[-1]) % p)

rlt = 0
for i in range(N-K+1):
  rlt += (As[-i-1] - As[i])*cmb(N-i-1,K-1,p)
  rlt %= p
  
print(rlt)