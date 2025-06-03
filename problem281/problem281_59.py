def mod_fact(N,p):
    mod=1
    for n in range(1,N+1):
        mod = (mod*(n%p))%p
        
    mod = mod%p
    
    return mod

X,Y = list(map(int,input().split()))

Z = X+Y

ans=0

if Z%3 != 0:
    ans=0
    
elif min(X,Y) >= Z//3:
    b=0
    for z in range(Z//3,((Z//3)*2)+1):
        if z == X:
            break
        b+=1
    a = Z//3 - b 
    
    p=(10**9)+7

    Z_= mod_fact(Z//3 , p)
    a_= mod_fact(a , p)
    b_= mod_fact(b , p)

    a_= pow(a_,p-2,p)
    b_= pow(b_,p-2,p)

    ans=(Z_*(a_*b_))%p
    
print(ans)
