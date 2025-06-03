import math
A,B = map(int, input().split())

a1 = math.ceil(A / 0.08)
a2 = math.floor((A+1) / 0.08)
b1 = math.ceil(B / 0.10)
b2 = math.floor((B+1) / 0.10)

dupl = set(range(a1, a2)) & set(range(b1, b2))
if len(dupl) > 0: 
    print(min(dupl))
else:
    print(-1)

