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

x = int(input())
while True:
    p = prime_factorize(x)
    if len(p) == 1:
        print(p[0])
        break
    x += 1