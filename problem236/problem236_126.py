import math
H = int(input())
W = int(input())
N = int(input())
ans = max([H,W])
fa = N/ans
print(math.ceil(fa))