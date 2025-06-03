while True:
    x,y = map(int, input().split())
    if not x and not y:
        break
    else:
        if x > y:
            print(y,x)
        else:
            print(x,y)