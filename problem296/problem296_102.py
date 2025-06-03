def input_list():
  return list(map(int, input().split()))


def main():
  s = list(input())
  k = int(input())
  if len(set(s)) == 1:
    print(int(len(s)*(k/2)))
    exit()
  
  sw = [s[0]]
  num = 0
  numbers = [num]
  for i in range(1, len(s)):
    if s[i-1] != s[i]:
      num += 1
    numbers.append(num)
    if num == 0 and sw[0] == s[i]:
      sw.append(s[i])

  num = 0
  end_w = s[-1]
  ew = []
  for i in range(len(s)-1, -1, -1):
    if end_w != s[i]:
      num += 1
    if num == 0 and end_w == s[i]:
      ew.append(s[i])
  nc = collections.Counter(numbers)
  
  a = 0
  for n,c in nc.items():
    if c == 1:
      continue
    if c % 2 == 0:
      a += c // 2
    else:
      a += (c-1)//2
  
  ans = a * k
  b = 0
  if ew[0] == sw[0]:
    haji = len(sw) + len(ew)
    if haji % 2 == 0:
      print(a * k + (k-1))
      exit()
  print(ans - b)
  
import math
import fractions
import collections
import itertools
from functools import reduce
main()