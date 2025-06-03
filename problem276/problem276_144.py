n=int(input())
a=[0]*n
a=list(map(int,input().split()))
left=a[0]
right=sum(a[1::])
t=abs(right-left)
for i in range(1,n):
  left+=a[i]
  right-=a[i]
  t=min(t,abs(right-left))
print(t)