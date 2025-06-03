n=int(input())
a=list(map(int,input().split()))
b=a+a
b.sort(reverse=True)
ans=0
for i in range(1,n):
  ans+=b[i]
print(ans)