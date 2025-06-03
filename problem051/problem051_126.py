while(True):
    H, W = map(int, input().strip().split())
    if(H == W == 0):
        break
    for x in range(H):
        print(''.join('#.'[(x + y) % 2] for y in range(W)))
    print()