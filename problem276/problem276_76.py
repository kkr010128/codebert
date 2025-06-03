def main():
    N = int(input())
    A = [int(a) for a in input().split()]

    s = [0 for i in range(N + 1)]
    for i in range(N):
        s[i + 1] = A[i] + s[i]

    ans = 10**10
    for i in range(1, N):
        l = s[i] - s[0]
        r = s[-1] - s[i]
        ans = min(ans, abs(l - r))

    print(ans)

if __name__ == "__main__":
    main()