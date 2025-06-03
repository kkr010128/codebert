while True:
    h,w = map(int,raw_input().split())
    if h == 0 and w == 0:
        break
    print "#" * w
    for a in range(h-2):
        print "#" + "."*(w-2) + "#"
    print "#" * w
    print ""