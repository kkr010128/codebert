# encoding:utf-8
while True:
    L = list(map(int, input().split(" ")))
    if L[0] == 0 and L[1] == 0:
        break
    L.sort()
    print("{0} {1}".format(L[0],L[1]))