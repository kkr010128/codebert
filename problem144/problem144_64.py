A,B,H,M = map(int, input().split())
import math
h = ((H*60+M)/720)*2*math.pi
m = (M/60)*2*math.pi
s = A*math.cos(h)-B*math.cos(m)
t = A*math.sin(h)-B*math.sin(m)
print((s**2 + t**2)**0.5)