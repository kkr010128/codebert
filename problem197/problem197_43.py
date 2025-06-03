from decimal import Decimal
import numpy as np
a, b, c = map(int, input().split())

if np.sqrt(Decimal(a)) + np.sqrt(Decimal(b)) < np.sqrt(Decimal(c)):
  print("Yes")
else:
  print("No")
