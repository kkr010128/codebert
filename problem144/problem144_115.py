import sys
import math
A,B,H,M=map(int, input().split())

print(math.sqrt(A**2+B**2-2*A*B*math.cos(math.radians(abs(30*(H+float(M/60))-6*M)))))