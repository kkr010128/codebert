#abc167_e
n,m,k = map(int,input().split())

mod = 998244353

ans = 0

#precalculation of the factorial
#fact[i] = i!
num = n
fact = [0] * num
fact[0] = 1
for i in range(1,num):
    fact[i] = (fact[i-1] * i) % mod

    
#precalculation of the (M-1)**i
#M_pow[i] = (M-1)^i
M_pow = [0] * num
M_pow[0] = 1
for i in range(1,num):
    M_pow[i] = (M_pow[i-1] * (m-1)) % mod


for i in range(k+1):
    f = M_pow[n-i-1] * pow(fact[i]*fact[n-i-1], mod-2, mod)
    ans += f % mod

ans *= m * fact[n-1]
print(ans % mod)