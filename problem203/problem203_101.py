import math
import sys
A,B = map(int,input().split())
for i in range(B*10,B*10+10):
    if math.floor(i * 0.08) == A and math.floor(i * 0.1) == B:
        print(i)
        sys.exit()
print(-1)