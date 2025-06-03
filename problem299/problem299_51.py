n=int(input())
a=[int(x) for x in input().rstrip().split()]
ans=[0 for i in range(n)] 
for i in range(n):
    ans[a[i]-1]=i+1
print(*ans)
