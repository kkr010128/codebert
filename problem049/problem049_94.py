while True:
    H,W = (int(x) for x in input().split())
    
    if H == 0 and W == 0:
        break
    
    i = 0 
    while i < H:
        j = 0 
        while j < W:
            print ("#", end='')
            j += 1
        print ('')
        i += 1
    print ('')
