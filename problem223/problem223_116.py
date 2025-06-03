from collections import defaultdict
from collections import deque
from collections import OrderedDict
import itertools
from sys import stdin
input = stdin.readline


def main():
  N, K = list(map(int, input().split()))
  P = list(map(int, input().split()))

  PP = [0]*N
  for i, p in enumerate(P):
    PP[i] = p*(p+1)/(2*p)

  S = [0]*(N+1)
  for i in range(1, N+1):
    S[i] = PP[i-1] + S[i-1]

  max_ = 0
  for i in range(0, N-K+1):
    max_ = max(max_, S[i+K] - S[i])

  print(max_)


if(__name__ == '__main__'):
  main()
