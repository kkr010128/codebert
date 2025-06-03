import math

x = raw_input()
x = float(x)

S = x*x*math.pi
l = 2*x*math.pi

print("%.6f %.6f" %(S, l))