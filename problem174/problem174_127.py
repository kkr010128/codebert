def main():
    from math import gcd
    K = int(input())
    ans = 0
    for a in range(1, K+1):
        for b in range(1, K+1):
            g = gcd(a, b)
            for c in range(1, K+1):
                ans += gcd(g, c)
    print(ans)


if __name__ == '__main__':
    main()
