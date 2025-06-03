N = int(input())
mod = int(1e9) + 7
def doubling(n, m):
    y = 1
    bas = n
    tmp = m
    while tmp:
        if tmp % 2:
            y *= bas
            y %= mod
        bas *= bas
        bas %= mod
        tmp >>= 1
    return y
d10 = doubling(10, N)
d9 = doubling(9, N)
d8 = doubling(8, N)
print((d10 - 2*d9 + d8) % mod)