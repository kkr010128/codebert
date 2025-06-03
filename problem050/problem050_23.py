
while True:
    H, W = map(int, input().split())
    if not(H or W):
        break
    for j in range(W):
        print('#', end='')
    print()
    for i in range(H-2):
        print('#', end='')
        for j in range(W-2):
            print('.', end='')
        print('#')
    for j in range(W):
        print('#', end='')
    print('\n')