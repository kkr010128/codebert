while True:
    [a,b] = raw_input().split()
    a = int(a)
    b = int(b)
    if a == 0 and b == 0:
        break
    if a < b:
        print a,b
    else:
        print b,a