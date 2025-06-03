def modpow(a, b, mod):
    ret = 1
    while b > 0:
        if b % 2 == 1:
            ret = ret * a % mod
        a = a * a % mod
        b //= 2
    return ret


mod = 10 ** 9 + 7
N, K = map(int, input().split())
LUT, ans = [0] * (K + 1), 0
for g in range(K, 0, -1):
    LUT[g] = modpow(K // g, N, mod)
    LUT[g] = (LUT[g] - sum([LUT[i] for i in range(g * 2, K + 1, g)])) % mod
for i in range(K + 1):
    ans = (ans + i * LUT[i]) % mod
print(ans)
