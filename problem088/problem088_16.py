import sys

n=int(input())
li=[int(x) for x in input().split()]

h=0
k=0

for i in range(n):
  if h<=li[i]:
    h=max(h,li[i])
  else:
    k=k+(h-li[i])
    h=max(h,li[i])
    
print(k)