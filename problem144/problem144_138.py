import math
A, B, H, M = map(int, input().split())
 
X, Y = A*math.cos(math.pi*(60*H+M)/360), -A*math.sin(math.pi*(60*H+M)/360)
x, y = B*math.cos(math.pi*M/30), -B*math.sin(math.pi*M/30)
 
print(math.sqrt((X-x)**2+(Y-y)**2))