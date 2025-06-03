def main():
    N, K = map(int, input().split())

    N %= K
    ans = abs(N-K)
    print(ans if ans < N else N)


if __name__ == '__main__':
    main()