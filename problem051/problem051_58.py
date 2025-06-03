while True:
    (H, W) = [int(i) for i in input().split()]
    if H == W == 0:
        break

    for a in range(H):
        for b in range(W):
            print('#', end='') if (a + b) % 2 == 0 else print('.', end='')
        print()
    print()