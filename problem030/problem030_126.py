import math

pi=math.pi

a,b,si=map(float,input().split())

S=(1/2)*a*b*math.sin(math.radians(si))
c2=a*a+b*b-2*a*b*math.cos(math.radians(si))
L=a+b+math.sqrt(c2)
h=(2*S)/a

print(S)
print(L)
print(h)
