def main():
    n, k = map(int, input().split())
    MOD = 10**9 + 7
    a = [0]*(k+1)
    for i in range(1, k+1):
        a[i] = pow(k//i, n, MOD)
    for i in reversed(range(1, k+1)):
        for j in range(2*i, k+1, i):
            a[i] -= a[j]
            a[i] %= MOD
    ans = 0
    for i in range(1, k+1):
        ans += a[i]*i
        ans %= MOD
    print(ans)

if __name__ == "__main__":
    main()