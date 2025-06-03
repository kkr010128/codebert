import sys

K = int(input())
A, B = (int(x) for x in input().split())
num=0
while B>=num:
  num+=K
  if A<=num and num<=B:
    print("OK")
    sys.exit(0)
print("NG")