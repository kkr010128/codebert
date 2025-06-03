import math
s = input().split(" ")
n = list(map(float,s))
d = math.sqrt((n[0]-n[2])**2 + (n[1]-n[3])**2)
print(d)