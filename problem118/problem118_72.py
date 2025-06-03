a=int(input())
b=(a)//2+1
ans=0
for i in range(1,b,1):
  x=a//i
  ans+=((x**2+x)//2)*i
ans+=(a**2+a+b-b**2)//2
print(ans)