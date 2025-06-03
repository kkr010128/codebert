x,n=[int(x) for x in input().split()]
if n!=0:
    p=[int(x) for x in input().split()]
    l=list(range(110))
    for i in p:
        l.remove(i)
    L=[]
    for i in l:
        L.append(abs(i-x))
    m=min(L)
    print(l[L.index(m)])
else:
    print(x)