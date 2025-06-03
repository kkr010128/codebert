import math
n, x, t = input().split()
answer = math.ceil(int(n) / int(x)) * int(t)
print(answer)
