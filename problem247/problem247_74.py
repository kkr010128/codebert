def main():
    from fractions import gcd
    from math import ceil

    n, m, *a = map(int, open(0).read().split())
    b = [0 for _ in range(n)]
    a.sort()

    for i, j in enumerate(a):
        c = 0
        while j % 2 == 0:
            c += 1
            j = j // 2
        a[i] = j
        b[i] = c

    if len(set(b)) > 1:
        print(0)
        exit()

    lcm = 1
    for i in a:
        lcm = (lcm * i) // gcd(lcm, i)

    k = b[0] - 1
    ans = ceil(m // 2 ** k // lcm / 2)
    print(ans)


if __name__ == "__main__":
    main()
