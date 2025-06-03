import numpy as np
 
X = int(input())
X_lcm = np.lcm(360, X)
print(X_lcm // X)