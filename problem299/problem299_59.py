n=int(input())
a=list(map(int,input().split()))
b=[0]*n
for i in range(0,n):
  b[a[i]-1]=i+1
ans=''
for i in range(n):
  ans+=str(b[i])+' '
print(ans)