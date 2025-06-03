MOD = 10 ** 9 + 7
N = int(input())

Sall = pow(10, N, MOD)
S0 = S9 = pow(9, N, MOD)
S09 = pow(8, N, MOD)

ans = (Sall - (S0 + S9 - S09)) % MOD
print(ans)