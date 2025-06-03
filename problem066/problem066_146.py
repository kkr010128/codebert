while True:
    a = list(input())
    if a[0] == "-":
        break
    b = int(input())
    d=0
    for i in range (b):
        c = int(input())
        d += c
    e = d % len(a)
    f = a[e:len(a)]+a[0:e]
    g = ''.join(f)
    print(g)

