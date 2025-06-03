x,y = map(int,raw_input().split())
if x==y:
    print x
else:
    if y>x:
        tmp = x
        x = y
        y = tmp
    i=2
    ans = 1
    al = []
    while i*i<=x:
        if x % i ==0:
            if y % i==0:
                al.append(i)
                x = x/i
                y = y/i
                continue
        i+=1
    if len(al)==0:
        pass
    else:
        for j in al:
            ans *= j
    print ans