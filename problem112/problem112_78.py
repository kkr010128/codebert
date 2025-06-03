def main():
    n, k = map(int, input().split())
    a = sorted([int(i) for i in input().split()], reverse=True)
    mod = 10**9 + 7
    p = 1
    if n == k:
        for ai in a:
            p = p * ai % mod
        print(p)
        return
    if a[0] < 0 and k % 2:
        for ai in a[:k]:
            p = p * ai % mod
        print(p)
        return
    b = sorted([(abs(ai), ai) for ai in a], reverse=True)
    s = 0
    for ba, bb in b[:k]:
        p = p * ba % mod
        if bb < 0:
            s += 1
    if s % 2 == 0:
        print(p)
        return
    pa, na, pb, nb = [-1] * 4
    for ba, bb in b[:k]:
        if bb < 0:
            na = ba
        else:
            pa = ba
    for ba, bb in b[k:][::-1]:
        if bb < 0:
            nb = ba
        else:
            pb = ba
    if pa == -1 or nb == -1:
        print(p * pb * pow(na, mod - 2, mod) % mod)
    elif pb == -1 or na == -1:
        print(p * nb * pow(pa, mod - 2, mod) % mod)
    elif pa * pb > na * nb:
        print(p * pb * pow(na, mod - 2, mod) % mod)
    else:
        print(p * nb * pow(pa, mod - 2, mod) % mod)


if __name__ == '__main__':
    main()
