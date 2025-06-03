import math
import collections

def main():
  N = int(input())
  A = map(int, input().split())
  
  l = collections.Counter(A)
  
  for key,value in l.items():
    if value >= 2:
      print('NO')
      return
  print('YES')
    
    
  
main()