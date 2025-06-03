import math as m

a,b,c=input().split()
a=int(a)
b=int(b)
c=int(c)
c=m.radians(c)
S=0.5*a*b*m.sin(c)
L=a+b+m.sqrt(a*a+b*b-2*a*b*m.cos(c))
H=b*m.sin(c)
print(S)
print(L)
print(H)