n=int(input())
a=list(map(int,input().split()))
b=a[0]
ans=0
for n in range(n):
  if a[n]>b:
    b=a[n]
  else:
    ans+=b-a[n]
print(ans)