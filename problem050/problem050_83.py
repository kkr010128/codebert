while True:
    line = input()
    data = line.split()
    h = int(data[0])
    w = int(data[1])
    if h == 0 and w == 0:
        break

    for i in range(h):   
        for j in range(w):
            if i == 0 or i == h -1:
                print("#", end="")
            else:
                if j == 0 or j == w -1:
                    print("#", end="")
                else:
                    print(".", end="")
        print("")
    print("")





