n,a,b=map(int,input().split())
res=n//(a+b)*a
if n%(a+b)>=a:
    res+=a
else:
    res+=n%(a+b)
        
print(res)