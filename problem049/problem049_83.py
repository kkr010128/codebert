while True:
    a=[int(x) for x in input().split()]
    if a[0]==a[1]==0:
        break
    else:
        for i in range(a[0]):
            print("#"*a[1])
    print("")