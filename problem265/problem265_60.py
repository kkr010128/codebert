def resolve():
    from decimal import Decimal
    N = Decimal(input())
    for X in range(1, 50000+1):
        if (int(X * 1.08) == N):
            print(X)
            return
    print(':(')

    return

resolve()