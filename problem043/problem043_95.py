while True:
    a=input()
    b=a.split()
    c=list()
    for d in b:
        c.append(int(d))
        
    if c[0]==0 and c[1]==0:
        break
    
    else:
        d=sorted(c)
        print(d[0],d[1])

