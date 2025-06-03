import sys                                               
for i in sys.stdin:
    lst = i.split(' ')
    lst = map(int, lst)
    lst.sort()

    n = 1
    maxn = 1
    while n*n <= lst[0]:
        if lst[0]%n == 0 and lst[1]%(lst[0]/n) == 0:
            print lst[0]/n
            break
        elif lst[0]%n == 0 and lst[1]%n == 0:
            maxn = n
        n = n+1
    else:
        print maxn
    sys.exit(0)