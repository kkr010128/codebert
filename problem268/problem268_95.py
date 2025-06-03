N=int(input())
A=list(map(int,input().split()))
a,b,c=0,0,0
ans=1
mod=10**9+7
for i in A:
    ans=ans*[a,b,c].count(i)%mod
    if i==a: a+=1
    elif i==b: b+=1
    elif i==c: c+=1
print(ans)