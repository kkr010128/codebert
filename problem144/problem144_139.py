import math
A,B,H,M= map(int,input().split())
kd_a=0.5*(M+60*H)
kd_b=6*M

rad=math.radians(kd_a-kd_b)

X=A**2+B**2-2*A*B*math.cos(rad)
print(X**0.5)