from math import ceil

a,b,c,d = map(int,input().split())

if ceil(c/b) <= ceil(a/d):
  print("Yes")
else:
  print("No")