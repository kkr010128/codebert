import sys
input = sys.stdin.readline
import math
 
def INT(): return int(input())
def MAPINT(): return map(int, input().split())
def LMAPINT(): return list(map(int, input().split()))
def STR(): return input()
def MAPSTR(): return map(str, input().split())
def LMAPSTR(): return list(map(str, input().split()))
 
f_inf = float('inf')
 
x, y = LMAPINT()
for i in range(x+1):
  for j in range(x+1):
    if i + j == x and i*2 + j*4 == y:
      print('Yes')
      exit()
print('No')