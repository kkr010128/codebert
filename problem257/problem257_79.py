import bisect,collections,copy,heapq,itertools,math,string
import numpy as np
import sys
sys.setrecursionlimit(10**7)

def _S(): return sys.stdin.readline().rstrip()
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def LS(): return list(sys.stdin.readline().rstrip().split())

N = I()
_a = LI()
#AB = [LI() for _ in range(N)]
#A,B = zip(*AB)
a = np.array(_a)
#C = np.zeros(N + 1)

if not np.amin(a)==1:
    print(-1)
    exit()

maxNumber = 1

for i in range(N):
  if a[i] == maxNumber:
      maxNumber += 1

print(N - (maxNumber-1))

# current = 0
# for i in range(1,200001):
#     position=[]
#     position = np.where(a[current:] == i)
#     if position ==[] or position[0] == []:
#         break
#     else:
#         current = position[0][0]
# print(current)
    


# if ans:
#     print('Yes')
# else:
#     print('No')