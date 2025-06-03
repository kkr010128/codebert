x=int(input())
ans=1
now=x
while now%360!=0:
    now+=x
    ans+=1
print(ans)