def main():
    mod = 998244353
    fact = [1, 1]
    for i in range(2, 400001):
        fact.append(fact[-1]*i % mod)

    def nCr(n, r):
        return pow(fact[n-r]*fact[r] % mod, mod-2, mod)*fact[n] % mod

    n, m, k = map(int, input().split())
    ans = 0
    for i in range(k+1):
        ans = (ans+m*pow(m-1, n-i-1, mod)*nCr(n-1, n-i-1)) % mod

    print(ans)


main()
