import collections

def cin():
    in_ = list(map(int,input().split()))
    if len(in_) == 1:  return in_[0]
    else:  return in_

def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:  f += 2
    if n != 1:  a.append(n)
    return a

A, B = cin()
A, B = min(A, B), max(A, B)
res = collections.Counter(prime_factorize(A))
keys = list(res.keys())
keys.append(1)
ans = 0
for i in keys:
    if B % i == 0:
        ans += 1
print(ans)