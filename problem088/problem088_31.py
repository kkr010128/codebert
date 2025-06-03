def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    h = A[0]
    for i in range(1, N):
        ans += max(0, h - A[i])
        h = max(h, A[i])
    print(ans)


if __name__ == '__main__':
    main()