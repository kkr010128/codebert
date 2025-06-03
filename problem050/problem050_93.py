while True:
    H, W = [int(i) for i in input().split()]
    if W == 0 and H == 0:
        break
    for i in range(0, H):
        if i == 0:
            print('#' * W)
        elif i == (H - 1):
            print('#' * W)
        elif H == 1:
            break
        else:
            print('#', '.' * (W - 2), '#', sep='')
    print()