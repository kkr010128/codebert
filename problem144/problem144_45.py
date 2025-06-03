import math
A,B,H,M=map(int,input().split())
M_rad = math.radians(M*6)
H_rad = math.radians(H*30+M*0.5)
rad = M_rad - H_rad
ans = math.sqrt(A**2+B**2-2*A*B*math.cos(rad))
print(ans)