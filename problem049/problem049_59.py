while True:
    H,W = map(int, input().split())
    if H == 0 and W == 0:
        break
    a = "#" * W
    for i in range(H):
        print(a)
    print()