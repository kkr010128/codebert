n=int(input())
x=list(map(float,input().split()))
y=list(map(float,input().split()))

d1=0
d2=0
d3=0
for i in range(n):
	d1+=abs(x[i]-y[i])
	d2+=(x[i]-y[i])**2
	d3+=abs(x[i]-y[i])**3

from math import pow
d2=pow(d2,(1.0/2.0))
d3=pow(d3,(1.0/3.0))
di=max([abs(x[i]-y[i]) for i in range(n)])

print(d1)
print(d2)
print(d3)
print(di)