n=int(input())
a=list(map(int,input().split()))
ans=0
for i,x in enumerate(a):
    i+=1
    if (i*x)%2==0:
        continue
    ans+=1
print(ans)