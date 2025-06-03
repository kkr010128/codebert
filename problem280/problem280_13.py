import bisect,collections,copy,heapq,itertools,math,string
import numpy as np
import sys
sys.setrecursionlimit(10**7)

def _S(): return sys.stdin.readline().rstrip()
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def LS(): return list(sys.stdin.readline().rstrip().split())

N = I()
#H,N = LI()
_XY = [LI() for _ in range(N)]
# X,Y = zip(*XY)
XY = np.array(_XY)
#C = np.zeros(N + 1)
# print(XY)

# print(np.linalg.norm(XY[1]-XY[0]))

def calcdis(p1,p2):
    return np.linalg.norm(p2-p1)

ans = []
for i in range(N):
    tmp = 0
    for j in range(N):
        if not i==j:
            # print(i,j)
            tmp += calcdis(XY[i],XY[j])
    ans.append(tmp)
print(np.average(ans))

# if ans:
#     print('Yes')
# else:
#     print('No')