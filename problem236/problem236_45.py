import math

h, w, n = [int(input()) for i in range(3)]
ans = 0
if h > w:
    print(math.ceil(n / h))
else:
    print(math.ceil(n / w))