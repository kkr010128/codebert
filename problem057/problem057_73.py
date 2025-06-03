while True:
    m, f, v = [int(n) for n in input().split()]

    if m == f == v == -1:
        break
    sum = m + f
    if m == -1 or f == -1:
        print("F")
    elif 80 <= sum:
        print("A")
    elif 65 <= sum < 80:
        print("B")
    elif 50 <= sum < 65:
        print("C")
    elif 30 <= sum < 50:
        if 50 <= v:
            print("C")
        else:
            print("D")
    else:
        print("F")