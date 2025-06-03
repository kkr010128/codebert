import re
import sys
try:
  a = int(input())
  if not 1 <= a <= 10:
    sys.exit()
  print(a+(a**2)+(a**3))
except:
  sys.exit()