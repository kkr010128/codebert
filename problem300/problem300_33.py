def main():
    N, M = (int(i) for i in input().split())

    def enum_divisors(n):
        # 約数列挙
        divs = set()
        for i in range(1, n+1):
            if i*i > n:
                break
            if n % i == 0:
                divs.add(i)
                if n//i != i:
                    # i が平方数でない
                    divs.add(n//i)
        return divs

    divs = enum_divisors(N) & enum_divisors(M)
    ans = 1
    v = 1
    from math import gcd
    for s in sorted(divs):
        if s == 1:
            continue
        if gcd(v, s) == 1:
            v *= s
            ans += 1
    print(ans)


if __name__ == '__main__':
    main()
