def main():
    n, k = list(map(int, input().split()))
    mod = 1000000007
    N = list(range(n + 1))
    mn = [0] * (n + 1)
    mx = [0] * (n + 1)
    mx[0] = n
    for i in range(1, n + 1):
        mn[i] = mn[i - 1] + N[i]
        mx[i] = mx[i - 1] + N[n - i]
    ans = 0
    for a, b in zip(mn[k - 1:], mx[k - 1:]):
        ans += b - a + 1
        ans %= mod
    print(ans)

if __name__ == '__main__':
    main()
