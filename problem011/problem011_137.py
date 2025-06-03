a, b = map(int, input().split())
c = []
if a > b:
    a, b = b, a
if b%a == 0:
    print(a)
else:
    while True:
        for i in range(a):
            x = i + 2
            #print(a, x)
            if a%x == 0:
                if b%x == 0:
                    c.append(x)
                    a = a//x
                    b = b//x
                    #print(c)
                    break
                elif b%(a//x) == 0:
                    c.append(a//x)
                    a = x
                    b = b//(a//x)
                    #print(c)
                    break
            #if x%1000 == 0:
                #print(x)
            if x > a**0.5:
                break
        if x > a**0.5:
            break
    s = 1
    for j in c:
        s = s * j
    print(s)

