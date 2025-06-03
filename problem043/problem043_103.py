while 1:
    x, y =map(int,input().split())
    if not x+y:break
    if x>y:x,y=y,x
    print(x,y)
