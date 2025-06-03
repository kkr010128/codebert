import numpy as np
import scipy as sp
import math

a, b, c = map(int, input().split())
d = a + b + c
if(d<22):
  print("win")
else:
  print("bust")