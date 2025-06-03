import math
a, b, c = map(float, input().split(' '))
c = c / 180 * math.pi
s = a * b * math.sin(c) / 2
l = a + b + pow((pow(a, 2) + pow(b, 2) - 2 * a * b * math.cos(c)), 0.5)
h = b * math.sin(c)
print('{0:.8f}'.format(s) + '\n' + '{0:.8f}'.format(l) + '\n' + '{0:.8f}'.format(h))
