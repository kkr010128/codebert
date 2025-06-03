def main():
    N = int(input())
    X = []
    Y = []

    for _ in range(N):
        x, y = (int(i) for i in input().split())
        X.append(x + y)
        Y.append(x - y)

    ans = max(max(X) - min(X), max(Y) - min(Y))
    print(ans)


if __name__ == '__main__':
    main()
