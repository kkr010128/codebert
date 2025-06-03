import numpy as np
data = np.array([int(x) for x in str(input())])

if data.sum() % 9 == 0:
  print("Yes")
else:
  print("No")
