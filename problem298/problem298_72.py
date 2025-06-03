import numpy as np
n,k = map(int,input().split())
h = np.array(list(map(int,input().split())))

print(len(h[k<=h]))