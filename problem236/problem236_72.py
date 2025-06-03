def main():
    h = int(input())
    w = int(input())
    n = int(input())

    a = max(h, w)

    print((n + a - 1) // a)


if __name__ == "__main__":
    main()
