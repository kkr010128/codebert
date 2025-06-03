def pfact(n):
    d = {}
    while n % 2 == 0:
        d[2] = 1 if 2 not in d else d[2] + 1
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            d[f] = 1 if f not in d else d[f] + 1
            n //= f
        else:
            f += 2
    if n != 1:
        d[n] = 1 if n not in d else d[n] + 1
    return d

a, b = map(int, input().split())
A = pfact(a)
B = pfact(b)
d = {}
ans = 1
for k in A.keys():
    if k in B:
        ans += 1
print(ans)
