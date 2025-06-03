import numpy as np
A,B,H,M=map(int,input().split())

M_angle=M*6
h_=0
if M_angle>0: 
    h_=30/(360/M_angle)
H_angle=H*5*6+h_
Angle=abs(H_angle-M_angle)
Cos=np.cos(np.deg2rad(Angle))

ans_=(A**2)+(B**2)-(2*A*B*Cos)
ans=ans_**0.5
print(ans)