n=int(input())
a=list(map(int,input().split()))
ans=1
c=[0,0,0]
for i in range(n):
  if a[i] not in c:
    ans=0
  else:
    ans*=c.count(a[i])
    ans%=1000000007
    c[c.index(a[i])]+=1
print(ans)