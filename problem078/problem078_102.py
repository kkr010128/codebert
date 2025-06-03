mod = 1000000007
n = int(input())
ans = pow(10,n,mod) - 2 * pow(9,n,mod) + pow(8,n,mod)
ans = (ans % mod + mod) % mod
print(ans)