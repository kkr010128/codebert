while True:
    H, W = list(map(int, input().split()))
    if H == 0 and W == 0:
        break
    for height in range(H):
        for wide in range(W):
            if height == 0 or height == H-1 or wide == 0 or wide == W-1:
                print('#', end='')
            else:
                print('.', end='')
        print('')
    print('')