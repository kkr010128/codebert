def main():
    n, k = map(int, input().split())

    # ダブリング
    d = 60
    to = [[0 for _ in range(n)]
          for _ in range(d)]  # to[i][j] : 町jから2**i回ワープした町
    to[0] = list(map(int, input().split()))

    for i in range(1, d):
        for j in range(n):
            to[i][j] = to[i - 1][to[i - 1][j] - 1]

    v = 1
    for i in range(d, -1, -1):
        l = 2 ** i  # 2**i回ワープする

        if l <= k:
            v = to[i][v - 1]
            k -= l

        if k == 0:
            break

    print(v)


if __name__ == "__main__":
    main()
