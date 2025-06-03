while True:
    

    l = input().split()
    h = int(l[0])
    w = int(l[1])
    
    if h == 0 and w == 0:
        break
    
    element = h*(w+1)

    for i in range(element):
        if (i+1)%(w+1) == 0:
            print("")
            if i == element-1:
                print("")
        elif i+1 < w or i+1 > element-w-1:
            print("#", end="")
        else:
            if (i+1)%(w+1) == 1 or (i+1)%(w+1) == w:
                   print("#", end="")
            else:
                   print(".", end="")