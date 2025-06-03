N = int(input())

ans = 0
MOD = 10**9+7

ans = 10**N-2*9**N+8**N
ans %= MOD
print(ans)