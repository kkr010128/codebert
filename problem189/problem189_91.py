def main():
    N, M = map(int, input().split())

    def choose_2(n):
        return n * (n - 1) // 2

    ans = choose_2(N + M) - N * M

    print(ans)


if __name__ == '__main__':
    main()
