import math
a = int(input())
b = int(input())
n = int(input())
dum = max(a,b)
ans = n/dum
print(math.ceil(ans))