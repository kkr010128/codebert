def main():
    from decimal import Decimal
    N, M = (Decimal(i) for i in input().split())
    print(int(N * M))


if __name__ == '__main__':
    main()
