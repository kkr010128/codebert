import math
n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
p=[1,2,3,math.inf]
p1=0
p2=0
p3=0
p4=0
 
#p=1
for i in range(n):
    p1+=(abs(a[i]-b[i]))
print("{:10f}".format(p1))
 
#p=2
q=0
for i in range(n):
    q+=((abs(a[i]-b[i]))**2)
    p2=math.sqrt(q)
print("{:10f}".format(p2))
 
#3
q=0
for i in range(n):
    q+=((abs(a[i]-b[i]))**3)
    p3=q**(1/3)
print("{:10f}".format(p3))
 
#inf
q=0
for i in range(n):
    q=(abs(a[i]-b[i]))
    if q>p4:
        p4=q 
print("{:10f}".format(p4))
