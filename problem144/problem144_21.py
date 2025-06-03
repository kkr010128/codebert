import math

a, b, h, m = map(int, input().split())

theta_a = (60*h+m)/720*2*math.pi
theta_b = m/60*2*math.pi
theta_a_b = abs(theta_a-theta_b)

ans = math.sqrt(a**2+b**2-2*a*b*math.cos(theta_a_b))
print(ans)