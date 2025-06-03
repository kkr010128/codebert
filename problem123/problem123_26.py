n=int(input())
a=list(map(int,input().split()))
res=0
for i in range(n):
  res^=a[i]
ans=[]
for i in range(n):
  ans.append(res^a[i])
print(*ans)