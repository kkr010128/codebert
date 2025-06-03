def main():
    N, A, B = map(int, input().split())

    if (B - A) % 2 == 0:
        print((B - A) // 2)
    else:
        ret = min(
            A + (B - A - 1) // 2,
            (N - B + 1) + (N - (A + N - B + 1)) // 2
        )
        print(ret)


if __name__ == '__main__':
    main()
