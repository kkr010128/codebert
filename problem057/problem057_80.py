while True:
    r = list(map(int, input().split()))

    if r[0] == -1 and r[1] == -1 and r[2] == -1:
        break
    elif r[0] == -1 or r[1] == -1:
        print("F")
    elif r[0] + r[1] >= 80:
        print("A")
    elif r[0] + r[1] >= 65 and r[0] + r[1] < 80:
        print("B")
    elif r[0] + r[1] >= 50 and r[0] + r[1] < 65:
        print("C")
    elif r[0] + r[1] >= 30 and r[0] + r[1] < 50:
        if r[2] >= 50:
            print("C")
        else:
            print("D")
    else:
        print("F")