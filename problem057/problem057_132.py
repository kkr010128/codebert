while True:
    m,f,r=map(int,input().split())
    a=0
    if m ==-1 and f==-1 and r==-1:
        break
    elif m==-1 or f==-1:
        a="F"
    elif m+f>=80:
        a="A"
    elif m+f>=65 and m+f<=79:
        a="B"
    elif m+f>=50 and m+f<=65:
        a="C"
    elif m+f>=30 and m+f<=49:
        if r>=50:
            a="C"
        else:
            a="D"
    elif m+f<=29:
        a="F"
    print(a)
