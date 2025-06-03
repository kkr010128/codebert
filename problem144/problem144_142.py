import math
A,B,H,M = map(int,input().split())

#短針は1分間に0.5度動くことに注意
dig = abs((H*30 + M*0.5)-M*6)
if dig > 180:
    dig = 360 - dig

ans = math.sqrt((A**2+B**2)-(2*A*B*math.cos(math.radians(dig))))
print(ans)