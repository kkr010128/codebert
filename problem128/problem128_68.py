X,N=map(int,input().split())
if N==0:
    print(X)
else:
    w=input()
    w=w.split()
    t=list(w)
    b=list(range(-150,151))
    tt=[int(a) for a in t]

    ttt=set(tt)
    bb=set(b)

    c=bb^ttt

    cc=list(c)

    u=1000


    for s in cc:
        if abs(s-X)<u:
            u=abs(s-X)

    if (X-u) in cc:
            print(X-u)
    else :
            print(X+u)