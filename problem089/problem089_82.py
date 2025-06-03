def main(): 
    h,w,m = map(int,input().split())
    X = [0]*w
    Y = [0]*h
    g = set([])
    for _ in range(m):
        a,b = map(int,input().split())
        a-=1
        b-=1
        X[b]+=1
        Y[a]+=1
        g.add((a,b))
    
    xmax = max(X)
    ymax = max(Y)

    xlist = []
    for i,x in enumerate(X):
        if x==xmax:
            xlist.append(i)
    ylist = []
    for i,y in enumerate(Y):
        if y==ymax:
            ylist.append(i)
    
    ans = xmax+ymax
    flag = True
    for x in xlist:
        for y in ylist:
            if (y,x) not in g:
                flag = False
                break
        if not flag:
            break
    
    if flag:
        ans-=1
    print(ans)
main()