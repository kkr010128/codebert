import math
a = int(input())
if a%2 == 0:
    print(int((a/2-1)))
else:
    b = int(math.floor(a/2))
    print(b)