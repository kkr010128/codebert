while True:
    h,w = tuple([int(x) for x in raw_input().split(" ")])
    if h==0 and w==0: break
    for _h in range(h):
        print "#" * w
    print ""