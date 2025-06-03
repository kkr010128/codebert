while 1:
    H, W = map(int, raw_input().split())
    if H == W == 0:
        break
    print ('#'*W + '\n')*H