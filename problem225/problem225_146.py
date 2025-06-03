import math
H,A=map(int,input().split())
if H<=A:
    print(1)
else:
    print(math.ceil(H/A))