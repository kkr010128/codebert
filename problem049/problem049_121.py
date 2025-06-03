def az12():
    while True:
        xs = raw_input().split()
        H,W = int(xs[0]),int(xs[1]) 
        if H==0 and W==0 : break
        for i in range(0,H):
            print "#"*W
        print
az12()