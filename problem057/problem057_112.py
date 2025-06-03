while True:
    try:
        m,f,r = map(int,input().split(" "))
        if m == -1:
            if f == -1:
                if r == -1:
                    break
        if m == -1 or f == -1:
            print("F")
            continue
        if m+f >= 80:
            print("A")
        if m+f >= 65 and m+f < 80:
            print("B")
        if m+f >= 50 and m+f < 65:
            print("C")
        if m+f >= 30 and m+f < 50:
            if r >= 50:
                print("C")
            else:
                print("D")
        if m+f < 30:
            print("F")
    except EOFError:
        break