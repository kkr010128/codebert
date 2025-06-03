(a,b,c,d,e)=map(int,input().split())

if a==c:
    t=d-b
    if e<=t:
        print(t-e)
    else:
        print(0)
    
if c>a:
    if b>d:
        t=60*(c-a)-b+d
        if e<=t:
            print(t-e)
        else:
            print(0)
        
        
    if b<=d:
        t=(c-a)*60+d-b
        if e<=t:
            print(t-e)
        else:
            print(0)
        

