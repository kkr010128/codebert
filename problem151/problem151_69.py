N, M, K = map(int, input().split())

MOD = 998244353
invmod = [pow(i, MOD-2, MOD) for i in range(200002)]

if N == 1:
  print(M)
  exit()

if M == 1:
  if K == N-1:
    print(1)
  else:
    print(0)
  exit()
  
now = M * pow(M-1, N-1, MOD)
ans = now
if K == 0:
  print(ans % MOD)
  exit()

for ki in range(1, K+1):
  now = now * invmod[M-1] * (N-ki) * invmod[ki] % MOD
  ans += now
  
print(ans % MOD)
