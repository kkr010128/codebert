N = int(input())
MOD = 10**9 + 7
val1 = pow(9,N,MOD)

val2 = pow(8,N,MOD)
ans = pow(10,N,MOD) - 2*val1 + val2
print(ans%MOD)