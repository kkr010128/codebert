from collections import defaultdict
from sys import stdin
input = stdin.readline


def main():
  N, X, Y = list(map(int, input().split()))

  dic = defaultdict(int)
  for l in range(1, N):
    for r in range(l+1, N+1):
      spath = r - l
      if l <= X and Y <= r:
        spath -= (Y-X-1)
      elif l <= X and X < r <= Y:
        spath = min(spath, X-l+1+Y-r)
      elif X <= l < Y and Y <= r:
        spath = min(spath, l-X+1+r-Y)
      elif X < l < Y and X < r < Y:
        spath = min(spath, l-X+1+Y-r)
      dic[spath] += 1

  for k in range(1, N):
    print(dic[k])


if(__name__ == '__main__'):
  main()
