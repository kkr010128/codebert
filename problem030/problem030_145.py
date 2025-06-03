import math
E=0
A,B,C=map(int,input().split())
print((1/2)*A*B*(math.sin(math.radians(C))))
print(((A**2)+(B**2)-2*A*B*(math.cos(math.radians(C))))**(1/2)+A+B)
print(((1/2)*A*B*(math.sin(math.radians(C))))*2/A)

