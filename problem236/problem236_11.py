def main(h: int, w: int, n: int):
    m = max(h, w)

    if n % m == 0:
        print(n // m)
    else:
        print((n // m) + 1)


if __name__ == "__main__":
    h = int(input())
    w = int(input())
    n = int(input())

    main(h, w, n)
