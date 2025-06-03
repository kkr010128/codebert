from collections import deque
import sys
sys.setrecursion = 10000000


def solve(): 
  n = int(input())
  print([1, 1, 1, 2, 1, 2, 1, 5, 2, 2, 1, 5, 1, 2, 1, 14, 1, 5, 1, 5, 2, 2, 1, 15, 2, 2, 5, 4, 1, 4, 1, 51][n-1])

solve()