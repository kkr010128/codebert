n = int(input())
A = list(map(int,input().split()))

def factorize(n):
    fct = []  # prime factor
    b, e = 2, 0  # base, exponent
    while b * b <= n:
        while n % b == 0:
            n = n // b
            e = e + 1
        if e > 0:
            fct.append((b, e))
        b, e = b + 1, 0
    if n > 1:
        fct.append((n, 1))
    return fct

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

pc = True

fac = [0]*(10**6+1)
for a in A:
    lst = factorize(a)
    for p in lst:
        if not fac[p[0]]:
            fac[p[0]] = 1
        else:
            pc = False
            break
    if not pc:
        break
if pc:
    print('pairwise coprime')
else:
    g = A[0]
    for i in range(1,n):
        g = gcd(g, A[i])
    if g == 1:
        print('setwise coprime')
    else:
        print('not coprime')