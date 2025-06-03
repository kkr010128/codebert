n=int(input())
a=list(map(int,input().split()))
ans=[]
p=0
for i in range(n):
  p=p^a[i]
  
for i in range(n):
  k=p^a[i]
  ans.append(k)
print(*ans)