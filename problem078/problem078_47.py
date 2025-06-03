n = int(input())

MOD = 10**9 + 7

ans = pow(10, n, MOD)-pow(9, n, MOD) - pow(9, n, MOD) + pow(8, n, MOD)

#負の処理
ans = (ans+MOD)%MOD

print(ans)