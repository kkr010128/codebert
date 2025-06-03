while True:
    x = []
    x = input().split( )
    y = [int(s) for s in x]
    if sum(y) == -3:
        break
    if y[0] == -1 or y[1] == -1:
        print("F")
    elif y[0] + y[1] < 30:
        print("F")
    elif y[0] + y[1] >= 30 and y[0] + y[1] <50:
        if y[2] >= 50:
            print("C")
        else:
            print("D")
    elif  y[0] + y[1] >= 50 and y[0] + y[1] <65:
        print("C")
    elif  y[0] + y[1] >= 65 and y[0] + y[1] <80:
        print("B")
    elif  y[0] + y[1] >= 80:
        print("A")
