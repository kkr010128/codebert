L,R,d=map(int,input().split())
ans=0

for i in range(R-L+1):
    if (L+i)%d==0:
        ans+=1
print(ans)