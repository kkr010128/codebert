def factorization(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            cnt = 0
            while n % i == 0:
                cnt += 1
                n //= i
            e[i] = max(e[i], cnt)

    if n != 1:
        e[n] = max(e[n], 1)


def mod_pow(a, n):
    res = 1
    while n > 0:
        if n & 1:
            res = res * a % mod
        a = a * a % mod
        n >>= 1
    return res


n = int(input())
a = list(map(int, input().split()))

mod = 10 ** 9 + 7
e = [0] * 10 ** 6

for v in a:
    factorization(v)

lcm = 1
for i, c in enumerate(e):
    if c > 0:
        lcm = lcm * mod_pow(i, c) % mod

res = 0
for v in a:
    res = (res + lcm * mod_pow(v, mod - 2)) % mod

print(res)