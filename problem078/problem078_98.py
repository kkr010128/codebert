MOD = 10**9 + 7

N = int(input())

x = pow(10, N, MOD)
x -= pow(9, N, MOD) * 2
x += pow(8, N, MOD)
print(x % MOD)