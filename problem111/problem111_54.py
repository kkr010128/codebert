n=int(input())
a=sorted(list(map(int,input().split())))[::-1]
ans=a[0]
for i in range(1,(n-2)//2+1):
  ans+=(a[i]*2)
if n%2:
  ans+=a[(n-2)//2+1]
print(ans)