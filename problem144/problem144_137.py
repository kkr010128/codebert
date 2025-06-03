import math
A,B,H,M = map(int,input().split())
arg_H = (360*H)/12+(30*M)/60
if M ==0:
    arg_M = 360
else:
    arg_M = (360*M)/60
HM = abs(arg_H-arg_M)
arg_HM = min(HM, 360-HM)
CM2 = A**2+B**2-2*A*B*math.cos(math.radians(arg_HM))
CM = math.sqrt(CM2)
print(CM)