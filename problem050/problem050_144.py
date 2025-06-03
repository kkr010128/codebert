import sys

d = sys.stdin.readlines()
for i in d:
    h, w = [int(x) for x in i.split()]
    if h == 0 and w == 0:
        break
    for j in range(h):
        if j == 0 or j == h - 1:
            print('#' * w)
        else:
            print('#' + '.' * (w - 2) + '#')
    print('')