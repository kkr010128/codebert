import math

a,b,H,M=map(int,input().split())

theta_a = math.pi/6 * (H+M/60)
theta_b = math.pi*2*M/60

ans = math.sqrt((b*math.cos(theta_b) - a*math.cos(theta_a))**2 + (b*math.sin(theta_b) - a*math.sin(theta_a))**2)

print(ans)