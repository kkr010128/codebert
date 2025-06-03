while True:
    H, W = list(map(int, input().split()))
    if H == 0 and W == 0:
        break
    for height in range(H):
        if height%2 == 0:
            flag = True
        else:
            flag = False
        for wide in range(W):
            if flag:
                print('#', end='')
            else:
                print('.', end='')
            flag = not(flag)
        print('')
    print('')