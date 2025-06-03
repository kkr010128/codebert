import math
n = int(input())
print((n // 2) / n if n % 2 == 0 else math.ceil(n / 2) / n)