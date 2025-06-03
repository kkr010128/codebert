while True:
    H, W = map(int, input().split())
    if not(H or W):
        break
    for i in range(H):
        print('#', end='')
        for j in range(W-2):
            if i > 0 and i < H - 1:
                print('.', end='')
            else:
                print('#', end='')
        print('#')
    print()