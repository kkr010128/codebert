while True:
    x,y = [int(i) for i in input().split()]
    if x == 0 and y == 0:
        break
    if x>y:
        print(str(y) + " " + str(x))
    else:
        print(str(x) + " " + str(y))
