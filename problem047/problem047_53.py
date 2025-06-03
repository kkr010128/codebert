while 1:
    x,y,z=raw_input().split()
    x=int(x)
    z=int(z)
    if(y=='?'):
        break
    if(y=='+'):
        print x+z
    if(y=='-'):
        print x-z
    if(y=='/'):
        print x/z
    if(y=='%'):
        print x%z
    if(y=='*'):
        print x*z