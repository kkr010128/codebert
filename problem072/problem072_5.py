def main() -> None:
    n = int(input())

    count = 0
    for _ in range(n):
        d1, d2 = map(int, input().split())
        if d1 == d2:
            count += 1
        else:
            count = 0
        if count == 3:
            print('Yes')
            return
    print('No')
    return


if __name__ == '__main__':
    main()
