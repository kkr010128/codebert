while True:
    (H, W) = [int(x) for x in input().split()]
    if H == W == 0:
        break

    for hc in range(H):
        [print('#', end='') for wc in range(W)]
        print()

    print()