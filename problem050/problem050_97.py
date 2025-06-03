def rect(h, w):
    s = '#' * w
    while h > 1:
        print(s)
        s = '#' + '.' * (w - 2) + '#'
        h -= 1
    print('#' * w)
    print()
    return

while True:
    n = list(map(int, input().split()))
    H = n[0]
    W = n[1]
    if (H == 0 and W == 0):
        break
    rect(H, W)