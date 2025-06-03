import math
A,B,C,D = list(map(int,input().split()))

if (math.ceil(C/B)-math.ceil(A/D))<1:
    print("Yes")
else:
    print("No")
