def main():
    n, k = map(int, input().split())
    MOD = 10 ** 9 + 7
    ans = 0
    cnt = [0] * (k + 1)
    for i in range(1, k + 1):
        cnt[i] = pow(k // i, n, MOD)
    for i in range(k, 0, -1):
        for j in range(2, k // i + 1):
            cnt[i] -= cnt[i * j]
    ans = 0
    for i, c in enumerate(cnt):
        ans += i * c
        ans %= MOD
    print(ans)
    

if __name__ == '__main__':
    main()