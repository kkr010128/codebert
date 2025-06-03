n=int(input())
a=[0]+[int(x) for x in input().split()]
ans=[0]*(n+1)

for i in range(len(a)):
    ans[a[i]]=i

ans.pop(0)

print(*ans)