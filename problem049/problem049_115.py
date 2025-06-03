while True:
    a = list(map(lambda x : int(x), input().split(" ")))
    if a[0] == 0 and a[1] == 0:
        break
    for i in range(a[0]):
        for j in range(a[1]):
            print("#", end="")
        print()
    print()