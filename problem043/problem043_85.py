c = 0
while True:
    a = input().split(' ')
    x = int(a[0])
    y = int(a[1])

    if (x or y) == 0:
        break;
    elif x < y:
        print(x,y)
    elif x > y:
        print(y,x)
    elif x == y:
        print(x,y)
    c += 1