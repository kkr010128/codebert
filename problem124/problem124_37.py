mod = 10 ** 9 + 7
k = int(input())
s = len(input())
n = s + k

fac = [1] * (n+1)
for i in range(1, n+1):
    fac[i] = fac[i-1] * i % mod

ans = 0
for i in range(s, n+1):
	ncr = fac[i-1] * pow(fac[i-s]*fac[s-1] % mod, mod-2, mod) % mod
	res = pow(26, n-i, mod)* pow(25, i-s, mod) % mod
	ans = (ans + res * ncr) % mod
print(ans) 

