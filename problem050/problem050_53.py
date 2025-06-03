while True :
    H, W = [int(temp) for temp in input().split()]
    
    if H == W == 0 :
        break
    
    for making in range(H):
        if making == 0 or making == (H - 1) : print('#' * W)
        else                                : print('#' + ('.' * (W - 2)) + '#')

    print()