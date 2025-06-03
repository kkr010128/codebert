
while True:
    x,y = raw_input().split()
    x,y = map(int,(x,y))
    if x == 0 and y == 0:
        break
    if x > y:
        x,y = map(str,(x,y))
        print y + " " + x
    else:
        x,y = map(str,(x,y))
        print x + " " + y