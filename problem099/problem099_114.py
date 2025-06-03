import sys
import numpy as np
import math
def Ii():return int(sys.stdin.readline())
def Mi():return map(int,sys.stdin.readline().split())
def Li():return list(map(int,sys.stdin.readline().split()))
n,k = Mi()
a = np.array(sys.stdin.readline().split(), np.int64)
maxa = np.max(a)
mina = maxa//(k+1)
while maxa > mina+1:
  mid = (mina+maxa)//2
  div = np.sum(np.ceil(a/mid-1))
  if div > k:
    mina = mid
  else:
    maxa = mid
  
print(maxa)