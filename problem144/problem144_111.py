import math

A, B, H, M = map(int,input().split(' '))


theta = abs( (H/12)+(M/60)*(1/12) - M/60 ) * 2*math.pi

ans = math.sqrt(B**2 * math.sin(theta)**2 + (B*math.cos(theta) -A) **2 )

print(ans)