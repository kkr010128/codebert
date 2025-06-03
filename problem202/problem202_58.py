n,a,b,=map(int,input().split())
c = n//(a+b)
da = n-c*(a+b)
if da>a:
  da=a
print(c*a+da)