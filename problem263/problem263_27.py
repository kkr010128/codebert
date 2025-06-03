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

cnt = [0] * 60
for v in a:
    for i in range(60):
        if (v >> i) & 1:
            cnt[i] += 1

pow_2 = [1]
for i in range(60):
    pow_2.append(pow_2[-1] * 2 % mod)

res = 0
for v in a:
    for i in range(60):
        if (v >> i) & 1:
            res = (res + (n - cnt[i]) * pow_2[i] % mod) % mod
        else:
            res = (res + cnt[i] * pow_2[i] % mod) % mod

print(res * mod_pow(2, mod - 2) % mod)