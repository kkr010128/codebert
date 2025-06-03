import math
in_line = raw_input().split()
a = float(in_line[0])
b = float(in_line[1])
c = float(in_line[2])
print 0.5*a*b*math.sin(math.radians(c))
print a+b+math.sqrt(a*a+b*b-2*a*b*math.cos(math.radians(c)))
print b*math.sin(math.radians(c))