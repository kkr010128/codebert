import math
L,R,d = map(int, input().strip().split())
x=math.ceil(L/d)
y=math.floor(R/d)
print(y-x+1)
