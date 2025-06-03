def main():
    N, R = map(int, input().split())

    X = R + max(0, 100 * (10 - N))

    print(X)


if __name__ == '__main__':
    main()
