while True:
    H, W = map(int, input().split())
    if not(H or W):
        break
    for i in range(H):
        for j in range(W):
            if (i + j) % 2:
                print('.', end='')
            else:
                print('#', end='')
        print()
    print()