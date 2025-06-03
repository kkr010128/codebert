def main():
    mod = pow(10, 9)+7
    k = int(input())
    s = input()
    n = len(s)
    ans = 0
    key = pow(26, k, mod)
    sub = 1
    c = 1
    for i in range(k+1):
        ans += key*sub*c
        ans %= mod
        sub *= 25
        sub %= mod
        key = key*pow(26, mod-2, mod)%mod
        c *= (n+i)
        c *= pow(i+1, mod-2, mod)
        c %= mod
    print(ans)

if __name__ == "__main__":
    main()
