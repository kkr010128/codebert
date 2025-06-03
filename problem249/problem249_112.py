def main():
    A, B, K = map(int, input().split())

    r = max(0, A + B - K)

    a = min(r, B)
    t = r - a

    print(t, a)


if __name__ == '__main__':
    main()
