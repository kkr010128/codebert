n=int(input())
a=list(map(int,input().split()))
ans=0
t=10**6
for i in range(n):
  if a[i]<t:
    ans+=1
    t=a[i]
print(ans)