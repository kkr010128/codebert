import math
import sys
import itertools
from collections import deque
# import numpy as np

def main():
  n = int(input())

  d = deque()
  for _ in range(n):
    order = input().split()

    if order[0] == 'insert':
      d.appendleft(order[1])
    elif order[0] == 'delete':
      try:
        d.remove(order[1])
      except ValueError:
        pass
    elif order[0] == 'deleteFirst':
      d.popleft()
    elif order[0] == 'deleteLast':
      d.pop()

  print(*d)

if __name__ == '__main__':
  main()
