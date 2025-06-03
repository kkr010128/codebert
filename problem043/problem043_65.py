while True:
    x,y = map(int,raw_input().split())
    if x+y == 0:
        break
    elif x>y:
        print y,x
    else:
    	print x,y