# coding: utf-8
while True:
    h, w = map(int, input().split())
    if h == 0 and w == 0:
        exit()
    else:
        print('#' * w)
        for _ in range(h - 2):
            print('#' + '.' * (w - 2) + '#')
        print('#' * w)
        print()
