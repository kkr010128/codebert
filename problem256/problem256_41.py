import math
import sys
input = sys.stdin.readline
a,b=map(int,input().split())
i=1
while True:
  if a*i % b == 0:
    print(a*i)
    break
  i+=1