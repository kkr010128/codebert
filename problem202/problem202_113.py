n,a,b=map(int, input().split())

if a==0:
    print(0)
    
elif b==0:
    print(n)
    
else:
    
    quo=n//(a+b)
    
    #商
    if n%(a+b)==0:
        rem=0
    elif  1<=n%(a+b)<=a:
        rem=n%(a+b)
    else:
        rem=a
        
    print(quo*a+rem)