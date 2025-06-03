import math
n = int(input())
c= [0]*n
s = map(int,input().split())

for i in s:
  c[i-1]+=1

for i in c:
  print(i)