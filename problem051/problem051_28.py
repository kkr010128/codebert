while True:
    H, W = [int(i) for i in input().split()]
    if H == W == 0:
        break
    for i in range(H):
        if i % 2 == 0:
            for j in range(W):
                if j % 2 == 0:
                    print('#', end='')
                else:
                    print('.', end='')
            else:
                print('')
        else:
            for j in range(W):
                if j % 2 == 0:
                    print('.', end='')
                else:
                    print('#', end='')
            else:
                print('')
    print('')