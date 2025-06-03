while 1:
    H, W = map(int, raw_input().split())
    if H == W == 0:
        break
    print '#'*W
    print ('#'+'.'*(W-2)+'#'+'\n')*(H-2)+'#'*W + '\n'