def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    mod = 10**9+7
    ans = 1
    s, t = [], []
    for i in range(n):
        if a[i] < 0:
            t.append(a[i])
        else:
            s.append(a[i])

    S, T = len(s), len(t)
    ok = False

    if S > 0:
        if n == k:
            ok = (T % 2 == 0)
        else:
            ok = True
    else:
        ok = (k % 2 == 0)

    if not ok:
        a.sort(key=abs)
        for i in range(k):
            ans *= a[i]
            ans %= mod
    else:
        s.sort()
        t.sort(reverse=True)
        if k % 2 == 1:
            ans *= s.pop()
            ans %= mod
        p = []
        while len(s) >= 2:
            x = s.pop()
            x *= s.pop()
            p.append(x)
        while len(t) >= 2:
            x = t.pop()
            x *= t.pop()
            p.append(x)
        p.sort(reverse=True)
        for i in range(k//2):
            ans *= p[i]
            ans %= mod
    print(ans)


if __name__ == '__main__':
    main()
