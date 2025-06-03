n,a,b=map(int,input().split())
t=a+b
if n%t<=a:
    diff=n%t
else:
    diff=a
print(a*(n//t)+diff)