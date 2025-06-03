import math

H = int(input())

ans = 2 ** int(math.log2(H) + 1) - 1

print(ans)
