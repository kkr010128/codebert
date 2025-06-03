import math
H = int(input())
W = int(input())
N = int(input())

if H >= W:
    print(math.ceil(N / H))
else:
    print(math.ceil(N / W))