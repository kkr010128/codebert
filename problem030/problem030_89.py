#coding = utf-8
import math
a, b, c = map(float, raw_input().split())
h = b * math.sin(math.pi*c/180)
s = a * h / 2
x = math.sqrt(h**2 + (a-b*math.sin(math.pi*(90-c)/180))**2) 
l = a + b + x
#print "%.8f, %.8f, %.8f" % (s, l, h)
print "\n".join([str(s), str(l), str(h)])
#print "%.1f, %.1f, %.1f" % (s, l, h)