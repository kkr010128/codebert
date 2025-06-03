n=int(input())
ans=0
for j,i in enumerate(input().split(),1):
    if int(i)%2 and j%2:
        ans+=1
print(ans)