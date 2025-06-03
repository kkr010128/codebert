while True:
    H, W = map(int, input().split())
    if not(H or W):
        break
    for i in range(H):
        print('#' * W)
    print()