def main():
    n = int(input())
    A = sorted(map(int, input().split()), reverse=True)
    ans = 0
    mod = 10 ** 9 + 7
    m=A[0]
    for i in range(61):
        cnt0 = cnt1 = 0
        if m < 2 ** i:
            break
        for j, a in enumerate(A):
            if a < 2 ** i:
                cnt0 += n - j
                break
            if (a >> i) & 1:
                cnt1 += 1
            else:
                cnt0 += 1
        ans += (((2 ** i) % mod) * ((cnt1 * cnt0) % mod)) % mod
        ans %= mod

    print(ans)

if __name__ == "__main__":
    main()