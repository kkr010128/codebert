import math


a, b, c = list(map(int, input().split()))
sa, sb, sc = math.sqrt(a), math.sqrt(b), math.sqrt(c)
d = c-a-b

if (c-a-b > 0) and ((c-a-b)**2 > 4*a*b):
    print("Yes")
else:
    print("No")
