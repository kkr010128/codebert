import math
h = int(input())
w = int(input())
n = int(input())
ans = math.ceil(n/max(h,w))
print(ans)