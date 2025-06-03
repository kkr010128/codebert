import math
data = map(float, raw_input().split(" "))

rad = data[2]*math.pi/180

h = data[1]*math.sin(rad)
s = data[0]*h/2
l = data[0]+data[1]+math.sqrt((data[0]-data[1]*math.cos(rad))**2+h**2)

print "%f\n%f\n%f" % (s,l,h)