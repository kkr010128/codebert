a,b = map(int,input().split())
if a >= b:
    i = 1
    while i > 0:
        if (a*i) % b == 0:
            print(a*i)
            break
        i += 1
else:
    i = 1
    while i > 0:
        if (a*i) % b == 0:
            print(a*i)
            break
        i += 1