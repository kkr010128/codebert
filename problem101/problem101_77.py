def main():
    a, b, c = [int(x) for x in input().split()]
    count = int(input())

    while a >= b:
        b *= 2
        count -= 1
    while b >= c:
        c *= 2
        count -= 1

    print('Yes' if count >= 0 else 'No')


if __name__ == '__main__':
    main()
