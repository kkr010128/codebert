n=int(input())
s=list(map(int,input().split()))

ans=0
j=1
for i in s:
    if i!=j :
        ans+=1
    else:
        j+=1
print(ans) if ans<n else print(-1)

