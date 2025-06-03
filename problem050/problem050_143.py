while True:
    H,W = map(int,input().split())
    if 3 <= H and W <= 300:
        print(W * ('#') +'\n' + (H - 2) * (('#' + (('.') * (W - 2)) + '#') + '\n') + W * ('#'))
    if H == W == 0:
        break
    print()