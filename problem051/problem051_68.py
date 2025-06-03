while True:    
    H, W = map(int, input().split())
    if H == 0 and W == 0:
        break
    else:
        if W % 2 == 0:
            i = H//2
            while i > 0:    
                print("#."*(W//2))
                print(".#"*(W//2))
                i -= 1
            if H % 2 == 1:
                print("#."*(W//2))
        else:
            i = H // 2
            while i > 0:    
                print("#."*(W//2)+"#")
                print(".#"*(W//2)+".")
                i -= 1
            if H % 2 == 1:
                print("#."*(W//2)+"#")
        print("")