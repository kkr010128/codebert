while True:
    H, W = map(int, raw_input().split())
    if H == 0 and W == 0:
        break
    s1 = ""
    s2 = ""
    for i in range(W):
        if i % 2 == 0:
            s1 += "#"
            s2 += "."
        else:
            s1 += "."
            s2 += "#"
    count = True
    for i in range(H):
        if count:
            print(s1)
        else:
            print(s2)
        count = not count
    print("")