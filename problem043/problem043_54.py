while True:
    a, b = map(int, input().split())
    if a==0 and b==0:
        break
    else:
        c = a,b
        d = sorted(c)
        print(d[0],d[1])