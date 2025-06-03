N=int(input())
ans=0
i=1
while i<=N:
    if i%2!=0:
        ans+=1
    i+=1

print(ans/N)
