def xgcd(a, b):
    x0, y0, x1, y1 = 1, 0, 0, 1
    while b != 0:
        q, a, b = a // b, b, a % b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return a, x0, y0

def invmod(a, m):
    g, x, y = xgcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

n, m, k = map(int, input().split())
ans = 0
c = 998244353

ans = m * pow(m-1, n-1, mod=c)
temp = 1
for i in range(1, k+1):
    temp = temp*(n-i) % c
    temp = temp*invmod(i, c) % c
    ans += temp * m * pow(m-1, n-1-i, mod=c)
    ans = ans % c
print(ans%c)