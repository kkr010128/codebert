X, Y = map(int, input().split())

m, r = divmod(2*Y-X, 3)
if r != 0:
    print(0)
    exit()

n = Y - 2*m

if n < 0 or m < 0:
    print(0)
    exit()

def modinv(a, mod=10**9+7):
    return pow(a, mod-2, mod)

def combination(n, r, mod=10**9+7):
    r = min(r, n-r)
    res = 1
    for i in range(r):
        res = res * (n-i) * modinv(i+1, mod) % mod
    return res

print(combination(n+m, n))