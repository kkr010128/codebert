import math

A,B,H,M = map(int,input().split())

print((A**2+B**2-2*A*B*math.cos(math.radians(6*M-30*(H+(M/60)))))**(1/2))