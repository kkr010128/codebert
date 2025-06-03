def main():
    n, m, k = map(int, input().split())
    mod = 998244353
    comb = 1
    c = 0
    for i in range(k + 1):
        if i > 0:
            comb = comb * (n - i) * pow(i, mod - 2, mod) % mod
        c = (c + m * comb * pow(m - 1, n - 1 - i, mod)) % mod
    print(c)

if __name__ == '__main__':
    main()