import collections
import sys
import math
sys.setrecursionlimit(10 ** 7)
def input() : return sys.stdin.readline().strip()
def INT()   : return int(input())
def MAP()   : return map(int,input().split())
def LIST()  : return list(MAP())
def NIJIGEN(H): return [list(input()) for i in range(H)]
K=int(input())
if K%2==0 or K%5==0:
  print(-1)
ans=7%K
for i in range(K):
  if ans==0:
    print(i+1)
    exit()
  ans=((ans*10)+7)%K