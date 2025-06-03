while(1):
    h,w = [int(i) for i in input().split()]
    if h == 0 and w == 0:
        break
    for i in range(h):
        print("#"*w)
    print("")
    
