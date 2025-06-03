import math
a,b,c=map(float,raw_input().split())
c = c / 180 * math.pi

print "%.10f" % float(a*b*math.sin(c)/2)
x = math.sqrt(a**2 + b**2 - 2 * a * b * math.cos(c))
print "%.10f" % float(a + b + x)
print "%.10f" % float(b*math.sin(c))