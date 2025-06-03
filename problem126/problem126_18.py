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

x = LMAPINT()
for i, y in enumerate(x):
  if y == 0:
    print(i+1)
    exit()