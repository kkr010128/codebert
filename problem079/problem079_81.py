MOD = 10**9 + 7

def modinv(a, mod=10**9+7):
    return pow(a, mod-2, mod)

def combination(n, r, mod=10**9+7):
    r = min(r, n-r)
    res = 1
    for i in range(r):
        res = res * (n - i) * modinv(i+1, mod) % mod
    return res




# print(combination(10,2))


s = int(input())
n = s//3
ans = 0
while n:
    S = s - n*3
    # print(S+n-1,n-1)
    ans += combination(S+n-1,n-1)
    n-=1

print(ans%MOD)