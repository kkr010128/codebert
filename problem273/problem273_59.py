import sys

read = sys.stdin.buffer.read
input = sys.stdin.buffer.readline
inputs = sys.stdin.buffer.readlines


# rstrip().decode('utf-8')
# INF=float("inf")
#MOD=10**9+7
# sys.setrecursionlimit(2147483647)
# import math
#import numpy as np
# import operator
# import bisect
# from heapq import heapify,heappop,heappush
#from math import gcd
# from fractions import gcd
#from collections import deque
from collections import defaultdict
# from collections import Counter
from itertools import accumulate
# from itertools import groupby
# from itertools import permutations
# from itertools import combinations
# from scipy.sparse import csr_matrix
# from scipy.sparse.csgraph import floyd_warshall
# from scipy.sparse.csgraph import csgraph_from_dense
# from scipy.sparse.csgraph import dijkstra
# map(int,input().split())


def main():
	n,k=map(int,input().split())
	A=list(map(int,input().split()))
	S=[0]+list(accumulate(A))
	for i in range(n+1):
		S[i]-=i
		S[i]%=k
	
	dct=defaultdict(int)
	
	ans=0
	for j in range(n+1):
		dct[S[j]]+=1
		if j>=k:
			dct[S[j-k]]-=1
		ans+=dct[S[j]]-1
	print(ans)
	
if __name__ == "__main__":
		main()
