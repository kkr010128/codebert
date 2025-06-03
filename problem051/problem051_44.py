while True:
    height, width = [int(x) for x in input().split(" ")]
    if height == width == 0:
        break

    a, b = "#", "."
    for h in range(height):
        for w in range(width):
            if w % 2 == 0: print(a,end="")
            else: print(b, end="")
        print("\n",end="")
        a, b = b, a


    print("\n", end="")