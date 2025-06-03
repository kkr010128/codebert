N, K = map(int, input().split())
A = list(map(int, input().split()))
A = sorted(A)
B = A[:][::-1]

fac = [1, 1]
finv = [1, 1]
inv = [0, 1]
Mod = 10**9+7
def COMinit():
  #N_C_kのN
  for i in range(2, 10**5+10):
    fac.append(fac[-1]*i%Mod)
    inv.append((-inv[Mod%i] * (Mod//i)) % Mod)
    finv.append(finv[-1] * inv[-1] % Mod)


def COM(n, k):
  if n < 0 or k < 0 or n < k:
    return 0
  return fac[n] * (finv[k] * finv[n-k] % Mod) % Mod

COMinit()

comb = {}
for i in range(K-1, N):
  comb[(i, K-1)] = COM(i, K-1)

ans = 0
for i in range(K-1, N):
  ans += A[i] * comb[(i, K-1)]
  ans %= Mod
for i in range(K-1, N):
  ans -= B[i] * comb[(i, K-1)]
  ans %= Mod
print(ans)

