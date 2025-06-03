import math

a,b,H,M=map(int,input().split())

theta_a = math.pi/6 * (H+M/60)
theta_b = math.pi*2*M/60

theta = abs(theta_a - theta_b)

ans = math.sqrt(a**2 + b**2 - 2*b*a*math.cos(theta))

print(ans)