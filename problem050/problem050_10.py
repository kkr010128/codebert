while(True):
    h, w = map(int, input().split())
    if w == 0 and h == 0:
        break

    print('#' * w)
    for i in range(0, h - 2):
        print('#' + '.' * (w - 2) + '#')
    print('#' * w)
    print()