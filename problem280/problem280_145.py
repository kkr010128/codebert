import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
 
import numpy as np
 
N = int(readline())
XY = np.array(read().split(),np.int64)
 
X = XY[::2]; Y = XY[1::2]
 
dx = X[:,None] - X[None,:]
dy = Y[:,None] - Y[None,:]
 
dist_mat = (dx * dx + dy * dy) ** .5
 
answer = dist_mat.sum() / N
print(answer)