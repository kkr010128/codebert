import math

A,B,H,M = map(int,input().split())

x = abs((60*H+M)*0.5 - M*6)
theta = math.radians(x)

L = (A**2+B**2-2*A*B*math.cos(theta))**(1/2)
print(L)