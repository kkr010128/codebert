import collections

zzz = 1
nn = int(input())
ans = 0

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
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a

for i in range(1,nn):
    zzz = 1
    cc = collections.Counter(prime_factorize(i))
    hoge = cc.values()
    for aaa in hoge:
        zzz *= aaa + 1
    ans += zzz
   
print(ans)