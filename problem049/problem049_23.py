while True:
    H, W = map(int, raw_input().split())
    if H == 0 or W == 0:
        break
    for _ in range(H):
        print '#' * W
    print ''