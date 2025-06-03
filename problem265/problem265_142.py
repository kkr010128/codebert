N = int(input())

import math
import sys

for i in range(1, 50000+1):
  if math.floor(i * 1.08) == N:
    print(i)
    sys.exit()
print(":(")