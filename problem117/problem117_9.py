import sys
import math
import itertools
import collections
from collections import deque

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()

NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()

def main():
    N, M, K = NMI()
    A = NLI()
    B = NLI()
    
    cumsum_A = [0 for _ in range(len(A)+1)]
    cumsum_B = [0 for _ in range(len(B)+1)]    
    
    cnt = 0
    
    for n in range(N):
        cnt += A[n]
        cumsum_A[n+1] = cnt
        
    cnt = 0
    
    for m in range(M):
        cnt += B[m]
        cumsum_B[m+1] = cnt
    

    
    ans = 0
    b= M
    
    for n in range(N+1):
        remain_K = K - cumsum_A[n]
        if remain_K < 0:
            break
        else:
            for m in range(b,-1,-1):
                if cumsum_B[m]> remain_K:
                    continue
                else:
                    b = m
                    ans = max(ans,n+m)
                break
    
    print(ans)
            
    


if __name__ == '__main__':
    main()