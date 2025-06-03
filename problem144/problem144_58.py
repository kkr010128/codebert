A,B,H,M = map(int, input().split())
m = M/60*360
h = H/12*360+M/60*30
kakudo = (h-m)%360
import math
cos = math.cos(math.radians(kakudo))
print(math.sqrt(A*A+B*B-2*A*B*cos))