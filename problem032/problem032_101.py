import math
ni = int(input())
xi = map(int, raw_input().split())
yi = map(int, raw_input().split())

p1 = []
p2 = []
p3 = []
p4 = []
for x, y in zip(xi, yi):
    p1.append(abs(x - y))
    p2.append(abs(x - y)**2)
    p3.append(abs(x - y)**3)
    p4.append(abs(x - y))

print '%.8f' % reduce(lambda x, y: x + y, p1)
print '%.8f' % reduce(lambda x, y: x + y, p2) ** (1.0/2.0)
print '%.8f' % reduce(lambda x, y: x + y, p3) ** (1.0/3.0)
print '%.8f' % max(p4)