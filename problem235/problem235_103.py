def resolve():
    def lcm(X, Y):
        x = X
        y = Y
        if y > x:
            x, y = y, x
        while x % y != 0:
            x, y = y, x % y
        return X * Y // y
    n = int(input())
    a = list(map(int, input().split()))
    mod = 10**9 + 7
    lsd = a[0]
    for i in range(1, n):
        lsd = lcm(lsd, a[i])
    lsd = lsd % mod

    ans = 0
    for i in range(n):
        ans += (lsd * pow(a[i], mod-2, mod)) % mod

    print(int(ans % mod))

resolve()