from  math import sqrt
n=int(input())
x=list(map(int,input().split()))
y=list(map(int,input().split()))
p1=0;p2=0;p3=0;p=[]
for i in range(n):
    a=abs(x[i]-y[i])
    p1+=a
    p2+=a**2
    p3+=a**3
    p.append(a)
print(p1)
print(sqrt(p2))
print(p3**(1/3))
print(max(p))
