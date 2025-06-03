while True:
    h,w = map(int,input().split())
    if h == 0 and w == 0:
        break
    for i in range(h):
        if i%2 == 1:
            sym1 = "#"
            sym2 = "."
        else:
            sym1 = "."
            sym2 = "#"

        for j in range(w):
            if j%2 == 1:
                print(sym1,end="")
            else:
                print(sym2,end="")
        print("")
    
    print("")