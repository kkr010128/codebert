from collections import defaultdict
from collections import deque
from collections import OrderedDict
import itertools
from sys import stdin
input = stdin.readline


def main():
  N = int(input())
  set_ = set()
  for i in range(N):
    set_.add(input()[:-1])

  print(len(set_))

if(__name__ == '__main__'):
  main()
