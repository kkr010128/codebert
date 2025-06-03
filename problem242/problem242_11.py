def cmb(n, r, p):
    if r < 0 or n < r:
        return 0
    r = min(r, n - r)
    return fact[n] * fact_inv[r] * fact_inv[n - r] % p


n, k = map(int, input().split())
a = sorted(list(map(int, input().split())), reverse=True)
p = 10 ** 9 + 7
fact = [1, 1]  # fact[n] = (n! mod p)
fact_inv = [1, 1]  # fact_inv[n] = ((n!)^(-1) mod p)
inv = [0, 1]  # fact_invの計算用

for i in range(2, n + 1):
    fact.append(fact[-1] * i % p)
    inv.append((-inv[p % i] * (p // i)) % p)
    fact_inv.append(fact_inv[-1] * inv[-1] % p)

i = 0
sum_max = 0
sum_min = 0
while n - i - 1 >= k - 1:
    cnt = cmb(n - i - 1, k - 1, p)
    sum_max += a[i] * cnt
    sum_min += a[n - i - 1] * cnt
    # print(i, a[i] * cnt, a[n - i - 1] * cnt)
    i += 1
ans = (sum_max - sum_min) % p
print(ans)
