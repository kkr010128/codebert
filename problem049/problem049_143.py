while 1:
    h, w = map(int, input().split())
    if h == w == 0: break
    
    for y in range(h):
        for x in range(w):
            print("#", end="")
        print("")

    print("")