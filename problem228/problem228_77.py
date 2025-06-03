import math
H = int(input())
print(2 ** (int(math.log(H, 2)) + 1 ) - 1)