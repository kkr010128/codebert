def main():
    n = int(input())
    print(b(n))


def b(n: int) -> int:
    m = 100
    i = 0
    while m < n:
        m = m * 101 // 100
        i += 1

    return i


if __name__ == '__main__':
    main()
