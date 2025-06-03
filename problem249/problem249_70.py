import numpy as np

inp = input()
A, B, K = int(inp.split(' ')[0]), int(inp.split(' ')[1]), int(inp.split(' ')[2])
  
if K>A:
  B = np.max([0, B-(K-A)])
A = np.max([0, A-K])

print(f'{A} {B}')