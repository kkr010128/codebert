import math
import collections
#2,4,5,7,9 hon
#0,1,6,8 pon
#3, bon
N = int(input())
a = N%10
B = [0,1,6,8]
if a == 3:
  print('bon')
elif a in B:
  print('pon')
else:
  print('hon')