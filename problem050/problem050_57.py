while True:
    H, W = map(int, input().split())
    if not(H or W):
        break
    print('#' * W)
    for i in range(H-2):
        print('#' + '.' * (W - 2), end='')
        print('#')
    print('#' * W, end='\n\n')