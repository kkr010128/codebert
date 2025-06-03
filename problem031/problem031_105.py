import math

def hensa(n, S):
 m = sum(S)/n
 x = 0
 for i in S:
  x += (i - m) ** 2
 hensa = math.sqrt(x / n)
 return hensa

n = int(input())
while n != 0:
 S = list(map(int, input().split()))
 print("{0:04f}".format(hensa(n, S)))
 n = int(input())