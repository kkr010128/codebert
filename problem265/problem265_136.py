import math
n = int(input())
og = n
n /= 1.08
n = math.ceil(n)
if int(n * 1.08) == og:
    print(n)
else:
    print(":(")
