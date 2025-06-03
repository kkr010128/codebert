while True:
    H, W = map(int, raw_input().split())
    if (H + W) == 0:
        break
    printW = ['#'] * W
    if W != 0:
        for h in range(H):
            print ''.join(printW)
    print ""