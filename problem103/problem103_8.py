def main():
    _ = int(input())
    *A, = map(int, input().split())
    A += [0]

    money = 1000
    stock = 0
    for a, b in zip(A, A[1:]):
        money += stock * a
        stock = 0
        if a < b:
            buy, rest = divmod(money, a)
            stock = buy
            money = rest
    print(money)


if __name__ == '__main__':
    main()
