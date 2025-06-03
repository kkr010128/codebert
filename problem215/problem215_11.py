MOD = 10**9 + 7
N = 10**6  # 10**6が限界
factorial_mod = [1, 1]  # factrial_mod[i] := i! mod p
modular_multiplicative_inverse = [0, 1]  # モジュラ逆数 := i^(-1) ≡ x (mod p) となるx
factorial_inverse_mod = [1, 1]  # factrial_inverse_mod[i] := (i!)^(-1) mod p

for i in range(2, N + 1):  # O(N)
    factorial_mod.append((factorial_mod[i - 1] * i) % MOD)
    modular_multiplicative_inverse.append((-modular_multiplicative_inverse[MOD % i] * (MOD // i)) % MOD)
    factorial_inverse_mod.append((factorial_inverse_mod[i-1] * modular_multiplicative_inverse[i]) % MOD)

def nCr_mod(n, r):
    if r < 0 or r > n:
        return 0
    r = min(r, n - r)
    return factorial_mod[n] * factorial_inverse_mod[r] * factorial_inverse_mod[n - r] % MOD

def nPr_mod(n, r):
    return factorial_mod[n] * factorial_inverse_mod[n - r] % MOD

# ---------------------- #

n, k = (int(x) for x in input().split())
ans = 0
for i in range(min(n - 1, k) + 1):
    # nCi * n-iHi = nCi * n-1Ci
    ans += nCr_mod(n, i) * nCr_mod(n - 1, i)
    ans %= MOD
print(ans)
