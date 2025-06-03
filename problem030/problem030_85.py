import math
a, b, C = map(int, input().split())
print('{0}'.format(0.5 * a * b * math.sin(C * math.pi / 180)))
print('{0}'.format(a + b + (a ** 2 + b ** 2 - 2 * a * b * math.cos(C * math.pi / 180)) ** 0.5))
print('{0}'.format(b * math.sin(C * math.pi / 180)))