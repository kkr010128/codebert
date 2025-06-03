n=int(input())
l=list(map(int,input().split()))
ans=[0]*n
for i in range(len(l)):
    ans[l[i]-1]=i+1
print(*ans)