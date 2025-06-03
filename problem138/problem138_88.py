class Inv:
  def __init__(s, mod):
    s.MOD = mod
  def modpow(s, a, n):
    res = 1
    while n > 0:
      if n & 1:
        res = res * a % s.MOD
      a = a * a % s.MOD
      n >>= 1
    return res
  def invx(s, a):
    return s.modpow(a, s.MOD - 2)
  def invpowL(s, a, n): # a^-x (0 <= x <= n)リスト
    ia = s.invx(a)
    L = [1] * (n + 1)
    for i in range(1, n + 1):
      L[i] = L[i - 1] * ia % s.MOD
    return L
  def invL(s, n): # 0 <= x <= n 逆元リスト
    I = [0, 1]
    for i in range(2, n + 1):
      I.append(s.MOD - I[s.MOD % i] * (s.MOD // i) % s.MOD)
    return I


N, S = list(map(int, input().split()))
A = list(map(int, input().split()))
MOD = 998244353

DP = [[0] * (S + 1) for _ in range(N + 1)]

inv = Inv(MOD)
v = inv.invx(2)

p = inv.modpow(2, N - 1)
for i in range(1, N + 1):
  a = A[i - 1]
  if a > S: 
    for j in range(S + 1):
      DP[i][j] = DP[i - 1][j]
    continue
  for j in range(a):
    DP[i][j] = DP[i - 1][j]
  DP[i][a] = (DP[i - 1][a] + p) % MOD
  for j in range(a + 1, S + 1):
    DP[i][j] = (DP[i - 1][j] + DP[i - 1][j - a] * v) % MOD

print(DP[-1][S])
