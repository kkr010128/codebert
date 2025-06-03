import math
p = map(float, raw_input().split())
print("%.10f" %(math.sqrt((p[2] - p[0]) * (p[2] - p[0]) + (p[3] - p[1]) * (p[3] - p[1]))))