import sys
input = sys.stdin.readline
K = int(input())
S = list(input())[: -1]
N = len(S)
mod = 10 ** 9 + 7

class Factorial:
  def __init__(self, n, mod):
    self.f = [1]
    for i in range(1, n + 1):
      self.f.append(self.f[-1] * i % mod)
    self.i = [pow(self.f[-1], mod - 2, mod)]
    for i in range(1, n + 1)[: : -1]:
      self.i.append(self.i[-1] * i % mod)
    self.i.reverse()
  def factorial(self, i):
    return self.f[i]
  def ifactorial(self, i):
    return self.i[i]
  def combi(self, n, k):
    return self.f[n] * self.i[n - k] % mod * self.i[k] % mod

f = Factorial(N + K + 1, mod)

res = 0
for l in range(K + 1):
  r = K - l
  res += f.combi(l + N - 1, l) * pow(25, l, mod) % mod * pow(26, r, mod) % mod
  res %= mod
print(res)