import math
from functools import reduce

def gcd_list(numbers):
  return reduce(math.gcd, numbers)

N=int(input())
A=list(map(int,input().split()))
mA = max(A)
D = [-1]*(mA+1)
D[0]=1
D[1]=1
for i in range(2,mA+1):
  if D[i] != -1: continue
  D[i] = i
  cnt = 2*i
  while cnt < mA+1:
    if D[cnt] == -1:
      D[cnt]=i
    cnt += i
done = set()
for a in A:
  tmp = set()
  while a > 1:
    tmp.add(D[a])
    a //= D[a]
  if len(done&tmp) > 0:
    if gcd_list(A) == 1: print('setwise coprime')
    else: print('not coprime')
    exit()
  done |= tmp
print('pairwise coprime')


