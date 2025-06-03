while True:
    x = [int(z) for z in input().split(" ")]
    if x[0] == 0 and x[1] == 0: break
    for h in range(0,x[0]):
        dot = h % 2
        for w in range(0,x[1]):
            if (dot == 0 and w % 2 == 0) or (dot == 1 and w % 2 == 1):
                print("#", end="")
            else:
                print(".", end="")
        print("\n", end="")
    print("")