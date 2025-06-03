import math
x1,y1,x2,y2=map(float,input().split())
A=abs(y1-y2)
B=abs(x1-x2)
C=math.sqrt(A**2+B**2)
print(f'{C:.8f}')
