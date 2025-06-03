def main():
    N = int(input())
    A = [int(i) for i in input().split()]
    ma = A[0]
    ans = 0
    for a in A:
        ma = max(ma, a)
        ans += ma - a
    print(ans)


if __name__ == '__main__':
    main()
