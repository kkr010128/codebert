while True:
    a=[int(x) for x in input().split()]
    if a[0]==a[1]==0:
        break
    else:
        print("#"*a[1])
        for i in range(a[0]-2):
            print("#"+"."*(a[1]-2)+"#")
        print("#"*a[1])
    print("")