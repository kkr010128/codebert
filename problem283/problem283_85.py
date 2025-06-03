#import numpy as np
#from numpy import*
#from scipy.sparse.csgraph import shortest_path #shortest_path(csgraph=graph) # dijkstra# floyd_warshall
#from scipy.sparse import csr_matrix
 
from collections import* #defaultdict Counter deque appendleft
from fractions import gcd
from functools import* #reduce
from itertools import* #permutations("AB",repeat=2) combinations("AB",2) product("AB",2) groupby accumulate
from operator import mul,itemgetter
from bisect import* #bisect_left bisect_right
from heapq import* #heapify heappop heappushpop
from math import factorial,pi
from copy import deepcopy
import sys
sys.setrecursionlimit(10**8)
#input=sys.stdin.readline

def main():
    n=int(input())
    ans=0
    for i in range(1,n):
        if (i!=n-i and i<n-i):
            ans+=1
        elif i>n-1:
            break
    print(ans)
    
    
if __name__ == '__main__':
    main()
