def main():
    import sys
    from collections import defaultdict
    input = sys.stdin.readline
    K = int(input())
    S = len(input().strip())
    mod = 10 ** 9 + 7
    fact = [1] * (K + S + 1)
    invfact = [1] * (K + S + 1)
    for i in range(K + S):
        fact[i+1] = (fact[i] * (i+1)) % mod
    invfact[-1] = pow(fact[-1], mod-2, mod)
    for i in range(K + S):
        invfact[-2-i] = (invfact[-1-i] * (K + S - i)) % mod
    def nCr(n, r):
        if r == n or r == 0:
            return 1
        r = min(r, n - r)
        return (fact[n] * invfact[n-r] * invfact[r]) % mod
    
    ans = 0
    for i in range(K+1):
        ans += pow(25, i, mod) * nCr(i+S-1, S-1) * pow(26, K-i, mod)
        ans %= mod

    print(ans)

if __name__ == '__main__':
    main()