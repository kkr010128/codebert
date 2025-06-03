import math
r = float(input())
#r = (float(x) for x in input().split())

d = r * r * math.pi 
R = 2 * r * math.pi
print ("{0:.6f} {1:.6f}".format(d,R))
