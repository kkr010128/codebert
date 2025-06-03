MOD = 10 ** 9 + 7

# エラトステネスの篩(コピペ用)
table_len = 1010
prime_list = [] # 必要に応じて
isprime = [True] * (1010)
isprime[0] = isprime[1] = False
for i in range(table_len):
    if isprime[i]:
        for j in range(2*i, table_len, i):
            isprime[j] = False
        prime_list.append(i) # 必要に応じて

N = int(input())
As = list(map(int, input().split()))
factor_counts = [0] * len(prime_list)
big_factors = set() # 1000より大きな素数がAの素因数として含まれるとき、その素因数は一乗のみだから
for A in As:
    for i, p in enumerate(prime_list):
        count = 0
        while A % p == 0:
            A //= p
            count += 1
        factor_counts[i] = max(factor_counts[i], count)
        if A == 1:
            break
    else:
        big_factors.add(A)

A_lcm = 1
for p, count in zip(prime_list, factor_counts):
    A_lcm *= pow(p, count, MOD)
    A_lcm %= MOD

for p in big_factors:
    A_lcm *= p
    A_lcm %= MOD

ans = 0
for A in As:
    ans += A_lcm * pow(A, MOD - 2, MOD) % MOD
    ans %= MOD

print(ans)