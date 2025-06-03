MOD = 10 ** 9 + 7

def inv(x):
  return pow(x, MOD - 2, MOD)


def gen_fact(n):
  fact = [1] * (n + 1)
  for i in range(2, n + 1):
    fact[i] = fact[i - 1] * i % MOD
  return fact


def binom(n, k, fact):
  assert 0 <= k <= n
  return fact[n] * inv(fact[k]) * inv(fact[n - k]) % MOD


def count(n, k, fact):
  n -= 3 * k
  return binom(n + k - 1, k - 1, fact)


if __name__ == '__main__':
  s = int(input())
  fact = gen_fact(s)
  res = 0
  for k in range(1, s // 3 + 1):
    res += count(s, k, fact)
  print(res % MOD)