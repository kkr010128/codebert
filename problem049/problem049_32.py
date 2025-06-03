while True:
    H, W = map(int, input().split())

    if H == 0 and W == 0:
        break

    square = [['#'] * W] * H
    for row in square:
        print(''.join(row))
    print()
