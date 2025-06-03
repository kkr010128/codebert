while True:
    a,b=map(int,input().split())
    if (a==0 and b==0):
        break
    if a>b:
        swap=a
        a=b
        b=swap       
    print('%d %d'%(a,b))


