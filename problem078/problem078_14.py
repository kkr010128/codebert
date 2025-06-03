N = int(input())
MOD = 10**9+7
ans = ((10**N%MOD - 9**N%MOD*2%MOD)%MOD + 8**N%MOD)%MOD
print(ans)