n=map(int,input().split())
*p,=map(int,input().split())

lmin=10**10
ans=0

for pp in p:
    ans+=1 if pp<=lmin else 0
    lmin=min(pp,lmin)

print(ans)
