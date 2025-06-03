n = int(input())
mod = 10**9+7

ans = pow(10,n)
ans -= pow(9,n)*2
ans += pow(8,n)

print(ans%mod)
