n=int(input())
table=[[0]*n for i in range(60)]
for i,v  in enumerate(map(int,input().split())):
    for j in range(60):
        table[j][n-1-i]=v%2
        v//=2
        if v==0:break
#print(*table,sep='\n')
ans=0
mod1,mod2=10**9+7,998244353
mod=mod1
a=1
for t in table:
    o,z=0,0
    
    for v in t:
        if v:
            o+=1
            ans=(ans+z*a)%mod
        else:
            z+=1
            ans=(ans+o*a)%mod

    a=a*2%mod
print(ans)