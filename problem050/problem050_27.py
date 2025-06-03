while True:
    height, width = [int(x) for x in input().split(" ")]
    if height == 0 and width ==0:
        break

    #start line
    print("{0}".format("#" * width))
    for h in range(0, (height - 2)):
        for w in range(width):
            if w == 0 or w == (width - 1):
                print ("#", end="")
            else:
                print (".", end="")
        print("\n", end="")


    #end line
    print("{0}".format("#" * width))

    print("\n", end="")