for i in range(1,10000):
    a = list(map(int,input().split()))
    if a[0]+a[1] == 0:
        break
    a.sort()
    print("{0[0]} {0[1]}".format(a))
