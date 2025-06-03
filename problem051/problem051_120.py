while True:
    
    l = input().split()
    h = int(l[0])
    w = int(l[1])

    if h == 0 and w ==0:
        break
    
    flag = 0

    for i in range(h*(w+1)):
        if (i+1) % (w+1) == 0:
            print("")
            if w % 2 == 0:
                flag += 1
            if i == h*(w+1)-1:
                print("")


        else:
            if flag % 2 == 0:
             print("#", end="")
             flag += 1
            else:
             print(".", end="")
             flag += 1