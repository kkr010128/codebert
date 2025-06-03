while True:
    h,w = map(int,input().split())
    if h == w == 0:
        break
    for x in range(int(h)):
        for y in range(int(w)):
            print("#",end="")
        print("")
    print("")