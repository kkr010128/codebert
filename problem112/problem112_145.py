MOD = 10 ** 9 + 7

# https://qiita.com/drken/items/3b4fdf0a78e7a138cd9a#3-1-mod-p-%E3%81%AE%E4%B8%96%E7%95%8C%E3%81%AB%E3%81%8A%E3%81%91%E3%82%8B%E5%89%B2%E3%82%8A%E7%AE%97%E3%81%A8%E3%81%AF


def modinv(a):
  b = MOD
  u = 1
  v = 0
  while b != 0:
    t = a // b
    a -= t * b
    a, b = b, a
    u -= t * v
    u, v = v, u
  u %= MOD
  if u < 0:
    u += MOD
  return u


n, k = list(map(int, input().split()))
a = list(map(int, input().split()))

# a = [e for e in a if e != 0]

# if len(a) < k:
#   print(0)
#   exit()

a.sort(key=lambda x: abs(x), reverse=True)

b = a[:k]
c = a[k:]

n = 0
pro_abs_b = 1
for e in b:
  if e < 0:
    n += 1
  pro_abs_b *= abs(e)
  pro_abs_b %= MOD
pro_b = (-1)**n * pro_abs_b % MOD

n_ = 0
pro_abs_ = 1
for e in a[len(a) - k:]:
  if e < 0:
    n_ += 1
  pro_abs_ *= abs(e)
  pro_abs_ %= MOD
pro_ = (-1) ** n_ * pro_abs_ % MOD

if n % 2 == 0:
  print(pro_b)
  exit()

anses = []
last_posinb = None
last_neginb = None
for e in b:
  if e > 0:
    last_posinb = e
  if e < 0:
    last_neginb = e
first_posinc = None
first_neginc = None
for e in reversed(c):
  if e > 0:
    first_posinc = e
  if e < 0:
    first_neginc = e

# print(last_posinb, last_neginb)
# print(first_posinc, first_neginc)
if last_posinb is not None and first_neginc is not None:
  anses.append((-first_neginc / last_posinb, pro_b *
                modinv(last_posinb) * first_neginc % MOD))
if last_neginb is not None and first_posinc is not None:
  anses.append((-first_posinc / last_neginb, pro_b *
                modinv(last_neginb) * first_posinc % MOD))

if len(anses) != 0:
  print(max(anses)[1])
else:
  print(pro_)
