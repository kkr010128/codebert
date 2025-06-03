n,a,b= list(map(int, input().strip().split()))
c=a+b
s=n//c
t=n%c
t=min(a,t)
print(a*s+t)