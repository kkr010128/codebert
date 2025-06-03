while True:
    h,w = map(int,input().split())
    if h == 0 and w == 0:
        break
    for x in range(h):
        if x == range(h)[0] or x == range(h)[-1]:
                print(w*"#",end="")
        else:
            for y in range(w):
                if y == range(w)[0] or y == range(w)[-1]:
                    print("#",end="")
                else:
                    print(".",end="")
        print()
    print()
