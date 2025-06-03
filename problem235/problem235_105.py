# import math
# import fractions

n = int(input())
a = list(map(int, input().split()))

mod = 10 ** 9 + 7


def prime_factorize(n):
    a = {}
    while n % 2 == 0:
        if 2 not in a:
          a[2] = 0
        a[2] += 1
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            if f not in a:
              a[f] = 0
            a[f] += 1
            n //= f
        else:
            f += 2
    if n != 1:
      if n not in a:
        a[n] = 0
      a[n] += 1
    return a


# 最小公倍数を素因数分解した形で持つ
l = prime_factorize(a[0])
# print(l)
# xs = {}
# xs[a[0]] = prime_factorize(a[0])
for i in range(1, n):
  ps = prime_factorize(a[i])
  # print(ps)
  # xs[a[i]] = ps
  for k, v in ps.items():
    if k in l:
      l[k] = max(v, l[k])
    else:
      l[k] = v

# print(l)
# print(xs)

L = 1
for k, v in l.items():
  L = L * pow(k, v, mod) % mod

answer = 0
for x in a:
  answer = (answer + L * pow(x, mod - 2, mod)) % mod
print(answer)
