# 素因数分解
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

  
a, b = map(int,input().split())
aa = prime_factorize(a)
bb = prime_factorize(b)
ab = list(set(aa) & set(bb))
ab.sort()
print(len(ab)+1)