H, W = list(map(int, input().split()))

while H != 0 or W != 0 :

    print('#' * W)
    for i in range(H-2) :
        print('#', end = '')
        print('.' * (W - 2), end = '')
        print('#')
    print('#' * W)
    print()
    H, W = list(map(int, input().split()))