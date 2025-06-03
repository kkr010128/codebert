N,K = map(int,input().split())

import numpy as np 

arr = np.array(input().split(),np.int64)

print(np.count_nonzero(arr>=K))