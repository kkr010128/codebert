for i in range(100000):
    h,w = map(int,input().split(" "))
    if h + w == 0:
        break
    print("#"*w)
    for j in range(h-2):
        print("#" + "."*(w-2) + "#")
    print("#"*w)
    print("")