import math
import numpy as np
A, B, H, M = [int(i) for i in input().split()]

ji = np.array([A*math.cos(-math.pi/6*(H+M/60) + math.pi/2), A*math.sin(-math.pi/6*(H+M/60) + math.pi/2)])

hun = np.array([B*math.cos(-math.pi/30*M + math.pi/2), B*math.sin(-math.pi/30*M + math.pi/2)])

print(math.sqrt(((ji-hun)**2).sum()))