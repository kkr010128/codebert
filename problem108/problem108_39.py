import math
n = int(input())
print((math.floor((n - 1) / 1000) + 1) * 1000 - n)