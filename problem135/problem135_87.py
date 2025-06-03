import math
a, b = map(str, input().split())
a2 = int(a)
b2 = int(b.replace('.', ''))
print(int((a2 * b2)//100))