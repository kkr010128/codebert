while True:
    x = [int(z) for z in input().split(" ")]
    if x[0] == 0 and x[1] == 0: break
    for h in range(0,x[0]):
        for w in range(0,x[1]):
            print("#", end="")
        print("\n", end="")
    print("")