H, W = map(int, input().split())
while H or W:
    for i in range(H):
        for j in range(W):
            print('#', end='')
        print()
    print()
    H, W = map(int, input().split())