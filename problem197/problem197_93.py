import numpy as np

a, b, c  = input().split()
a = int(a)
b = int(b)
c = int(c)

left = 4 * a * b
right = (c - (a + b)) ** 2

judge = c - (a + b)

if(judge < 0):
  print("No")
else:
  if(left < right):
  	print("Yes")
  else:
  	print("No")