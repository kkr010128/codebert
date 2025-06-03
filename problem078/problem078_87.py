N = int(input())
MOD = 10**9+7

a10 = 10**N
a9 = 9**N
a8 = 8**N
print((a10-a9-a9+a8) % MOD)
