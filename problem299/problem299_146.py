N=int(input())
import numpy as np
h=np.array(list(map(int,input().split())))
print(*(np.argsort(h)+1).tolist(), sep=' ')