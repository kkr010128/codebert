import sys
for line in sys.stdin:
    H, W = map(int, line.split())
    if H == W == 0:
        break
    print('#' * W)
    print(('#' + '.' * (W - 2) + '#\n') * (H - 2), end='')
    print('#' * W)
    print()