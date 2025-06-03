x,k,d=list(map(int,input().split()))
#print(x,k,d)
result=abs(x)-k*d
swithn=0

if result<0:
    if k%2==1:
        x-=d
    result=min(x%(2*d),-x%(2*d))
print(result)