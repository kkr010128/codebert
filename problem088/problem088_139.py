n=int(input())
a=list(map(int,input().split()))
ans=0
step=0
for i in range(n-1):
  if a[i]+step<=a[i+1]:
    step=0
  else:
    ans+=a[i]+step-a[i+1]
    step=a[i]+step-a[i+1]
print(ans)