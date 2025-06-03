import math
a, b, c = map(int, input().split())
PI = 3.1415926535897932384
c = math.radians(c)
print('{:.5f}'.format(a * b * math.sin(c) / 2))
A = a - b * math.cos(c)
B = b * math.sin(c)
print('{:.5f}'.format(math.sqrt(A * A + B * B) + a + b))
print('{:.5f}'.format(B))

