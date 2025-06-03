M=10**9+7
x,y=map(int,input().split())
ans=0
if (x+y)%3==0:
  a=(2*y-x)//3
  b=(2*x-y)//3
  if a>=0 and b>=0:
    f1,f2=1,1
    for i in range(a+1,a+b+1):
      f1*=i
      f1%=M
    for i in range(1,b+1):
      f2*=i
      f2%=M
    ans=f1*pow(f2,M-2,M)

print(ans%M)
