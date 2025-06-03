import bisect,collections,copy,heapq,itertools,math,string
import numpy as np
import sys
sys.setrecursionlimit(10**7)

def _S(): return sys.stdin.readline().rstrip()
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def LS(): return list(sys.stdin.readline().rstrip().split())

N =I()
_P= LI()
#AB = [LI() for _ in range(N)]
#A,B = zip(*AB)
P = np.array(_P)
#C = np.zeros(N + 1)


def main():
    # count = 1
    # # if (len(P)==1):
    # #     return count
    # min_array =[P[0]]
    # for i in range(1,N):
    #     if (P[i]<=min_array[i-1]):
    #         count += 1    
    #     if P[i-1]>P[i]:
    #         min_array.append(P[i])
    #     else:
    #         min_array.append(P[i-1])
    # return count
# print(min_array)
    Q = np.minimum.accumulate(P)
    count = np.count_nonzero(P <= Q)
    return count

print(main())
# if ans:
#     print('Yes')
# else:
#     print('No')